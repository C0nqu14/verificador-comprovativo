from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from utils.extrair_texto import extrair_texto_arquivo
from utils.metadados import obter_metadados
from utils.localizacao import obter_localizacao_por_ip

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/verificar', methods=['POST'])
def verificar():
    if 'ficheiro' not in request.files:
        return jsonify({'erro': 'Nenhum arquivo enviado'}), 400

    file = request.files['ficheiro']
    if file.filename == '':
        return jsonify({'erro': 'Nome do arquivo vazio'}), 400

    if file and permitido(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        texto_extraido = extrair_texto_arquivo(filepath)
        metadados = obter_metadados(filepath)
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        localizacao_ip = obter_localizacao_por_ip(ip)

    
        palavras_chave_validas = ['multicaixa', 'bfa',  'bic', 'bai' , 'bci' 'comprovativo', 'transferência', 'iban']
        resultado_OCR = 'Válido' if any(p in texto_extraido.lower() for p in palavras_chave_validas) else 'Suspeito'

   
        resultado_metadados = 'Metadados válidos' if metadados else 'Metadados ausentes ou inválidos'

    
        tem_localizacao = localizacao_ip and localizacao_ip.get('pais') is not None

        score = 0
        if resultado_OCR == 'Válido':
            score += 40
        if resultado_metadados == 'Metadados válidos':
            score += 40
        if tem_localizacao:
            score += 20

        if score >= 80:
            status = 'Confiável'
        elif score >= 60:
            status = 'Aceitável'
        else:
            status = 'Suspeito'

        return jsonify({
            'status': status,
            'score_confiabilidade': f"{score}%",
            'resultado_OCR': resultado_OCR,
            'resultado_metadados': resultado_metadados,
            'texto_extraido': texto_extraido,
            'metadados_extraidos': metadados,
            'localizacao_ip': localizacao_ip,
            'explicacao': 'Análise baseada em texto, metadados e IP. Use esses dados para avaliar a autenticidade do comprovativo.'
        })

    return jsonify({'erro': 'Tipo de arquivo não permitido'}), 400

if __name__ == '__main__':
    app.run(debug=True)
