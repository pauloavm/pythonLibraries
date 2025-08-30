import random

class EscolherElemento:
    def __init__(self, lista):
        self.lista = lista

    def escolher(self):
        return random.choice(self.lista)

opcoes = ['Maçã', 'Banana', 'Laranja', 'Morango']
escolhedor = EscolherElemento(opcoes)
print("Elemento Escolhido Aleatoriamente:", escolhedor.escolher())
