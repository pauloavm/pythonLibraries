import random

class AmostragemAleatoria:
    def __init__(self, populacao, tamanho_amostra):
        self.populacao = populacao
        self.tamanho_amostra = tamanho_amostra

    def amostra(self):
        return random.sample(self.populacao, self.tamanho_amostra)

populacao = range(1, 101)
tamanho_amostra = 10
amostrador = AmostragemAleatoria(populacao, tamanho_amostra)
print("Amostra Aleatória da População:", amostrador.amostra())
