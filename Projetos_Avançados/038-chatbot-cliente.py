class Chatbot:
    def __init__(self):
        self.respostas = {
            "Olá": "Olá! Como posso ajudar?",
            "Como está o tempo hoje?": "Desculpe, eu sou apenas um chatbot e não tenho acesso às informações meteorológicas.",
            "Qual é o seu nome?": "Meu nome é ChatGPT, um assistente virtual.",
            "Onde você mora?": "Eu não tenho um local físico de moradia, pois sou um programa de computador.",
            "O que você pode fazer?": "Posso responder a perguntas, fornecer informações e ajudar com tarefas simples.",
            "Obrigado": "De nada! Se precisar de mais ajuda, é só perguntar."
        }

    def responder(self, pergunta):
        if pergunta in self.respostas:
            return self.respostas[pergunta]
        else:
            return "Desculpe, não entendi a pergunta. Você pode reformulá-la?"

chatbot = Chatbot()

while True:
    pergunta = input("Você: ")
    resposta = chatbot.responder(pergunta)
    print(f"Chatbot: {resposta}")