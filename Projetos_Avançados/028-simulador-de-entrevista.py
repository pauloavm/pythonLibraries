import random

# Defina sua lista de perguntas e respostas no formato (pergunta, resposta)
perguntas_respostas = [
    ("O que é Python?", "Python é uma linguagem de programação de alto nível."),
    ("Como você define uma lista vazia em Python?", "Você pode definir uma lista vazia usando 'lista = []' ou 'lista = list()'."),
    # Adicione mais perguntas e respostas aqui
]

def fazer_pergunta():
    # Seleciona uma pergunta aleatória da lista
    pergunta, resposta = random.choice(perguntas_respostas)
    
    # Faz a pergunta e obtém a resposta do usuário
    print("Pergunta:", pergunta)
    sua_resposta = input("Sua resposta: ").strip().lower()
    
    # Verifica se a resposta está correta
    if sua_resposta == resposta.lower():
        print("Correto! Parabéns.")
    else:
        print("Incorreto. A resposta correta é:", resposta)

def main():
    print("Bem-vindo ao seu simulador de entrevista de programação!")
    while True:
        fazer_pergunta()
        continuar = input("Deseja continuar estudando? (s/n): ").strip().lower()
        if continuar != 's':
            print("Obrigado por estudar!")
            break

if __name__ == "__main__":
    main()