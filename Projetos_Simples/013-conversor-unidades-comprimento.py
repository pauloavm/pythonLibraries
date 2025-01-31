def converter_comprimento(valor, unidade_origem, unidade_destino):
    unidades = {"metros": 1, "centímetros": 100, "milímetros": 1000, "quilômetros": 0.001, "polegadas": 39.37, "pés": 3.281}
    resultado = valor * unidades[unidade_origem] / unidades[unidade_destino]
    return resultado

valor = float(input("Digite o valor: "))
unidade_origem = input("Digite a unidade de origem (por exemplo, 'metros'): ").lower()
unidade_destino = input("Digite a unidade de destino (por exemplo, 'centímetros'): ").lower()

resultado = converter_comprimento(valor, unidade_origem, unidade_destino)
print(f"{valor} {unidade_origem} equivalem a {resultado} {unidade_destino}")