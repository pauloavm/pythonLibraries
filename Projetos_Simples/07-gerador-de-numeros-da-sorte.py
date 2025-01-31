import random

def gerar_numeros_da_sorte(qtd_numeros):
    numeros = random.sample(range(1, 101), qtd_numeros)
    return sorted(numeros)

qtd_numeros = int(input('Digite a quantidade de números da sorte desejados: '))
numeros_sorteados = gerar_numeros_da_sorte(qtd_numeros)
print(f'Números da sorte: {numeros_sorteados}')