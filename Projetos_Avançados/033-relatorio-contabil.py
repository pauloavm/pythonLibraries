import os
from PIL import Image
import pytesseract

# Função para extrair texto de uma imagem usando OCR
def extrair_texto_imagem(imagem):
    texto = pytesseract.image_to_string(Image.open(imagem))
    return texto

# Diretório onde estão as imagens dos recibos
diretorio_recibos = 'diretorio_dos_recibos'

# Lista para armazenar os textos extraídos dos recibos
textos_recibos = []

# Percorre os recibos no diretório e extrai o texto de cada um
for arquivo in os.listdir(diretorio_recibos):
    if arquivo.endswith('.png') or arquivo.endswith('.jpg'):
        texto_recibo = extrair_texto_imagem(os.path.join(diretorio_recibos, arquivo))
        textos_recibos.append(texto_recibo)

# Função para calcular as despesas com base nos textos extraídos
def calcular_despesas(textos_recibos):
    total_despesas = 0
    # Implemente aqui a lógica para calcular as despesas a partir do texto dos recibos
    # Exemplo simples: procurar por valores numéricos nos textos e somá-los
    for texto_recibo in textos_recibos:
        valores = [float(s) for s in texto_recibo.split() if s.replace('.', '', 1).isdigit()]
        total_despesas += sum(valores)
    return total_despesas

# Calcula o total de despesas
total = calcular_despesas(textos_recibos)

# Gera o relatório
relatorio = f"Total de despesas no mês: R$ {total:.2f}"
print(relatorio)