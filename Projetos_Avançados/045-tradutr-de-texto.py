from googletrans import Translator

import asyncio

async def translate_text():
    translator = Translator()

    # Solicitar ao usuário o texto a ser traduzido
    text = input("Digite o texto que você deseja traduzir: ")

    # Solicitar ao usuário o idioma de destino
    target_language = input("Digite o código do idioma de destino (por exemplo, 'en' para inglês): ")

try:
    # Traduzir o texto
    translation = await translator.translate(text, dest=target_language)

    # Exibir a tradução
    print(f"Texto Original: {text}")
    print(f"Tradução ({target_language}): {translation.text}")

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

asyncio.run(translate_text())in__:
print("Bem-vindo ao Tradutor de Texto!")

translate_text()