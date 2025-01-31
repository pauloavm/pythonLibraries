import math

def calculadora_cientifica():
    print("Calculadora Científica")
    while True:
        print("Opções:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Seno")
        print("6. Cosseno")
        print("7. Tangente")
        print("8. Logaritmo Natural")
        print("9. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "9":
            print("Saindo da Calculadora Científica. Até a próxima!")
            break

        if escolha in ("1", "2", "3", "4"):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == "1":
                resultado = num1 + num2
            elif escolha == "2":
                resultado = num1 - num2
            elif escolha == "3":
                resultado = num1 * num2
            elif escolha == "4":
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Erro: Divisão por zero!")
                    continue

        elif escolha in ("5", "6", "7"):
            angulo = float(input("Digite o ângulo em graus: "))

            if escolha == "5":
                resultado = math.sin(math.radians(angulo))
            elif escolha == "6":
                resultado = math.cos(math.radians(angulo))
            elif escolha == "7":
                if math.cos(math.radians(angulo)) != 0:
                    resultado = math.tan(math.radians(angulo))
                else:
                    print("Erro: Tangente não definida para esse ângulo!")
                    continue

        elif escolha == "8":
            num = float(input("Digite o número: "))

            if num > 0:
                resultado = math.log(num)
            else:
                print("Erro: Logaritmo não definido para números não positivos!")
                continue

        else:
            print("Opção inválida!")
            continue

        print(f"Resultado: {resultado}")

calculadora_cientifica()