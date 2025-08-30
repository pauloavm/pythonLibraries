import random


class LancamentoDados:
    def __init__(self):
        pass

    def lancar_dado(self):
        return random.randint(1, 6)


lancador = LancamentoDados()
print("Resultado do lançamento do dado:", lancador.lancar_dado())
