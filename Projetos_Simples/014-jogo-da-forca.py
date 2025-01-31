import random

palavras = ["python", "programação",
            "desenvolvimento", "computador", "curso"]

palavra_escolhida = random.choice(palavras)
palavra_adivinhada = ["_"] * len(palavra_escolhida)
tentativas = 6

print("Jogo da Forca")

while tentativas > 0 and "_" in palavra_adivinhada:  # Verifica se ainda há letras para adivinhar e tentativas restantes
    print(" ".join(palavra_adivinhada))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_escolhida:
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == letra:
                palavra_adivinhada[i] = letra
    else:
        tentativas -= 1
        print(
            f"Letra '{letra}' não encontrada. Você tem {tentativas} tentativas restantes.")

if "_" not in palavra_adivinhada:
    print("Parabéns! Você venceu. A palavra era:", palavra_escolhida)
else:
    print("Você perdeu! A palavra era:", palavra_escolhida)