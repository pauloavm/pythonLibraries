import os

class RenomearArquivo:
    def __init__(self, nome_antigo, nome_novo):
        self.nome_antigo = nome_antigo
        self.nome_novo = nome_novo

    def renomear(self):
        os.rename(self.nome_antigo, self.nome_novo)
        print("Arquivo renomeado de", self.nome_antigo, "para", self.nome_novo)

arquivo_antigo = "arquivo_antigo.txt"
arquivo_novo = "arquivo_novo.txt"
renomeador = RenomearArquivo(arquivo_antigo, arquivo_novo)
renomeador.renomear()
