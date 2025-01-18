import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

if __name__ == "__main__":
    comprimento_senha = int(input("Digite o comprimento da senha desejada: "))
    senha_gerada = gerar_senha(comprimento_senha)
    print(f"Sua senha segura gerada é: {senha_gerada}")