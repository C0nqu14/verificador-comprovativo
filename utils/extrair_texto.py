import pytesseract
from PIL import Image
import fitz  # PyMuPDF

def extrair_texto_arquivo(path):
    if path.lower().endswith('.pdf'):
        texto = ""
        doc = fitz.open(path)
        for page in doc:
            texto += page.get_text()
        doc.close()
        return texto.strip()
    else:
        imagem = Image.open(path)
        return pytesseract.image_to_string(imagem).strip()
