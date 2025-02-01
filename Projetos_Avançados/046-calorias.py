class CalculadoraDeCalorias:
    def __init__(self):
        self.refeicoes = []

    def adicionar_refeicao(self, nome_refeicao, calorias):
        self.refeicoes.append({"nome": nome_refeicao, "calorias": calorias})

    def calcular_calorias_diarias(self):
        total_calorias = sum(refeicao["calorias"] for refeicao in self.refeicoes)
        return total_calorias

    def ver_refeicoes(self):
        print("Refeições registradas:")
        for refeicao in self.refeicoes:
            print(f"{refeicao['nome']} - {refeicao['calorias']} calorias")

if __name__ == "__main__":
    calculadora = CalculadoraDeCalorias()

    while True:
        print("\nMenu:")
        print("1. Adicionar Refeição")
        print("2. Calcular Calorias Diárias")
        print("3. Ver Refeições Registradas")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_refeicao = input("Nome da refeição: ")
            calorias = float(input("Número de calorias: "))
            calculadora.adicionar_refeicao(nome_refeicao, calorias)
            print(f"{nome_refeicao} adicionada com sucesso!")
        elif escolha == "2":
            calorias_totais = calculadora.calcular_calorias_diarias()
            print(f"Total de calorias diárias: {calorias_totais} calorias")
        elif escolha == "3":
            calculadora.ver_refeicoes()
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")