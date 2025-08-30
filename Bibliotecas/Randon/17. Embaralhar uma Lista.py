import random


class EmbaralhadorLista:
    def __init__(self, lista):
        self.lista = lista

    def embaralhar(self):
        random.shuffle(self.lista)
        return self.lista


minha_lista = [1, 2, 3, 4, 5]
embaralhador = EmbaralhadorLista(minha_lista)
print("Lista Embaralhada:", embaralhador.embaralhar())
