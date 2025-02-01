import random

def jogar_jogo():
    opcoes = ['pedra', 'papel', 'tesoura']
    pontuacao_usuario = 0
    pontuacao_computador = 0

    print("Bem-vindo ao Jogo Pedra, Papel ou Tesoura!")
    
    while True:
        escolha_usuario = input("Escolha pedra, papel ou tesoura (ou 'sair' para sair): ").lower()
        
        if escolha_usuario == 'sair':
            break

        if escolha_usuario not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue

        escolha_computador = random.choice(opcoes)

        print(f"Você escolheu: {escolha_usuario}")
        print(f"O computador escolheu: {escolha_computador}")

        if escolha_usuario == escolha_computador:
            print("Empate!")
        elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
             (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
             (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
            print("Você venceu!")
            pontuacao_usuario += 1
        else:
            print("O computador venceu!")
            pontuacao_computador += 1

        print(f"Pontuação: Você {pontuacao_usuario}, Computador {pontuacao_computador}")
    
    print("Obrigado por jogar!")

if __name__ == "__main__":
    jogar_jogo()