import os

class VerificarDiretorio:
    def __init__(self, nome):
        self.nome = nome

    def verificar(self):
        if os.path.exists(self.nome):
            print("O diretório", self.nome, "existe.")
        else:
            print("O diretório", self.nome, "não existe.")

diretorio_verificar = "meu_diretorio"
verificador = VerificarDiretorio(diretorio_verificar)
verificador.verificar()
