lista_compras = []

while True:
    print("Lista de Compras")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Mostrar lista")
    print("4. Sair")

    escolha = input("Escolha uma opção (1/2/3/4): ")

    if escolha == "1":
        item = input("Digite o nome do item a ser adicionado: ")
        lista_compras.append(item)
        print(f"{item} foi adicionado à lista de compras.")
    elif escolha == "2":
        if not lista_compras:
            print("A lista de compras está vazia.")
        else:
            print("Itens na lista de compras:")
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")
            indice = int(input("Digite o número do item a ser removido: "))
            if 1 <= indice <= len(lista_compras):
                item_removido = lista_compras.pop(indice - 1)
                print(f"{item_removido} foi removido da lista de compras.")
            else:
                print("Índice inválido.")
    elif escolha == "3":
        if not lista_compras:
            print("A lista de compras está vazia.")
        else:
            print("Itens na lista de compras:")
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")
    elif escolha == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")