# Biblioteca de conversão de unidades
def converter_unidades(valor, de_unidade, para_unidade):
    # Implemente a lógica de conversão para várias unidades aqui
    if de_unidade == "kg" and para_unidade == "lb":
        return valor * 2.20462
    elif de_unidade == "km" and para_unidade == "mi":
        return valor * 0.621371
    elif de_unidade == "C" and para_unidade == "F":
        return (valor * 9/5) + 32
    else:
        return "Conversão não suportada"

if __name__ == "__main__":
    print("Bem-vindo ao Conversor de Unidades Avançado!")
    valor = float(input("Digite o valor a ser convertido: "))
    de_unidade = input("Digite a unidade de origem (por exemplo, kg, km, C): ")
    para_unidade = input("Digite a unidade de destino (por exemplo, lb, mi, F): ")

    resultado = converter_unidades(valor, de_unidade, para_unidade)

    if resultado != "Conversão não suportada":
        print(f"{valor} {de_unidade} equivale a {resultado} {para_unidade}")
    else:
        print(resultado)