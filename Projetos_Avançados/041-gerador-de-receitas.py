class Receita:
    def __init__(self, nome, ingredientes, instrucoes):
        self.nome = nome
        self.ingredientes = ingredientes
        self.instrucoes = instrucoes

class AplicativoReceitas:
    def __init__(self):
        self.receitas = []

    def adicionar_receita(self, nome, ingredientes, instrucoes):
        nova_receita = Receita(nome, ingredientes, instrucoes)
        self.receitas.append(nova_receita)
        print("Receita adicionada com sucesso!")

    def buscar_receita(self, nome):
        for receita in self.receitas:
            if receita.nome.lower() == nome.lower():
                print(f"--- {receita.nome} ---")
                print("Ingredientes:")
                for ingrediente in receita.ingredientes:
                    print(ingrediente)
                print("Instruções:")
                for instrucao in receita.instrucoes:
                    print(instrucao)
                return
        print("Receita não encontrada.")

    def listar_receitas(self):
        print("Lista de Receitas:")
        for receita in self.receitas:
            print(receita.nome)


if __name__ == "__main__":
    app = AplicativoReceitas()

    while True:
        print("\n=== Aplicativo de Receitas ===")
        print("1. Adicionar Receita")
        print("2. Buscar Receita")
        print("3. Listar Receitas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da receita: ")
            ingredientes = input("Ingredientes (separados por vírgula): ").split(", ")
            instrucoes = input("Instruções (separadas por ponto e vírgula): ").split("; ")
            app.adicionar_receita(nome, ingredientes, instrucoes)
        elif opcao == "2":
            nome = input("Digite o nome da receita que deseja buscar: ")
            app.buscar_receita(nome)
        elif opcao == "3":
            app.listar_receitas()
        elif opcao == "4":
            print("Obrigado por usar o aplicativo de receitas!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")