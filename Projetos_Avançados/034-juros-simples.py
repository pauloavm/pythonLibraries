def calcular_juros_simples(capital, taxa, tempo):
    juros = capital * (taxa / 100) * tempo
    montante = capital + juros
    return juros, montante

if __name__ == "__main__":
    print("Calculadora de Juros Simples")
    capital = float(input("Digite o valor do capital: R$"))
    taxa = float(input("Digite a taxa de juros (porcentagem): "))
    tempo = float(input("Digite o período de tempo (em anos): "))

    juros, montante = calcular_juros_simples(capital, taxa, tempo)

    print(f"Juros: R${juros:.2f}")
    print(f"Montante total: R${montante:.2f}")