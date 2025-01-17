import random

def lançar_dados(qtd_dados, lados_dados):
    resultados = [random.randint(1, lados_dados) for _ in range(qtd_dados)]
    return resultados

qtd_dados = int(input("Digite a quantidade de dados: "))
lados_dados = int(input("Digite o número de lados em cada dado: "))

resultados = lançar_dados(qtd_dados, lados_dados)
print(f"Resultados dos dados: {resultados}")