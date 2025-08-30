from datetime import datetime

class VerificarAnoBissexto:
    def __init__(self, ano):
        self.ano = ano

    def eh_bissexto(self):
        return (self.ano % 4 == 0 and self.ano % 100 != 0) or (self.ano % 400 == 0)

ano = 2024
verificador = VerificarAnoBissexto(ano)
if verificador.eh_bissexto():
    print(ano, "é um ano bissexto")
else:
    print(ano, "não é um ano bissexto")
