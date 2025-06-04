from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
from PyPDF2 import PdfReader

def obter_metadados(path):
    ext = os.path.splitext(path)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png']:
        try:
            imagem = Image.open(path)
            info = imagem._getexif()
            if not info:
                return {'info': 'Sem metadados'}
            dados = {}
            for tag, valor in info.items():
                nome = TAGS.get(tag, tag)
                if nome == "GPSInfo":
                    gps_dados = {}
                    for t in valor:
                        subtag = GPSTAGS.get(t, t)
                        gps_dados[subtag] = valor[t]
                    dados['GPSInfo'] = gps_dados
                else:
                    dados[nome] = valor
            return dados
        except Exception as e:
            return {'erro': str(e)}
    elif ext == '.pdf':
        try:
            reader = PdfReader(path)
            info = reader.metadata
            return {k[1:]: v for k, v in info.items()} if info else {'info': 'PDF sem metadados visíveis.'}
        except Exception as e:
            return {'erro': str(e)}
    else:
        return {'info': 'Tipo de arquivo não suportado para metadados'}
