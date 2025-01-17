dicionario_traducao = {
    "hello": "olá",
    "world": "mundo",
    "python": "Python",
    "programming": "programação",
    "learning": "aprendizado"
}

texto = input("Digite o texto a ser traduzido: ")

palavras = texto.split()
texto_traduzido = []

for palavra in palavras:
    traducao = dicionario_traducao.get(palavra.lower(), palavra)
    texto_traduzido.append(traducao)

texto_final = " ".join(texto_traduzido)
print("Texto traduzido:", texto_final)