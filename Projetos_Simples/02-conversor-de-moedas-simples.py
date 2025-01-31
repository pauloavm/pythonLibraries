def converter_moeda(valor, taxa):
    return valor * taxa

valor = float(input('Digite o valor em sua moeda: '))
taxa = float(input('Digite a taxa de câmbio: '))

resultado = converter_moeda(valor, taxa)
print(f'O valor convertido é: {resultado}')