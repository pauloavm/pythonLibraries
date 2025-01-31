import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

comprimento = int(input('Digite o comprimento da senha desejada: '))
senha = gerar_senha(comprimento)
print(f'Sua senha gerada é: {senha}')