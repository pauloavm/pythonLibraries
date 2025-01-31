def calcular_juros_compostos(capital, taxa, tempo):
    montante = capital * (1 + taxa / 100) ** tempo
    juros = montante - capital
    return juros, montante

if __name__ == "__main__":
    print("Calculadora de Juros Compostos")
    capital = float(input("Digite o valor do capital: R$"))
    taxa = float(input("Digite a taxa de juros (porcentagem): "))
    tempo = float(input("Digite o período de tempo (em anos): "))

    juros, montante = calcular_juros_compostos(capital, taxa, tempo)

    print(f"Juros: R${juros:.2f}")
    print(f"Montante total: R${montante:.2f}")