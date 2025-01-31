def calcular_gorjeta(conta, percentagem_gorjeta):
    gorjeta = conta * (percentagem_gorjeta / 100)
    total_conta = conta + gorjeta
    return gorjeta, total_conta

conta = float(input("Digite o valor da conta: R$ "))
percentagem_gorjeta = float(input("Digite a percentagem de gorjeta que deseja deixar (por exemplo, 10%): "))

gorjeta, total_conta = calcular_gorjeta(conta, percentagem_gorjeta)
print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Total da conta com gorjeta: R$ {total_conta:.2f}")