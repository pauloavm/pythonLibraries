"""CUIDADO AO USAR ESTE CÓDIGO!"""
"""CUIDADO AO URAR ESTE CÓDIGO!"""
"""CUIDADO AO URAR ESTE CÓDIGO!"""
# Este código exclui um arquivo do sistema operacional.

import os

class ExcluirArquivo:
    def __init__(self, nome):
        self.nome = nome

    def excluir(self):
        os.remove(self.nome)
        print("Arquivo", self.nome, "excluído com sucesso.")

arquivo_a_excluir = "arquivo_a_excluir.txt"
excluidor = ExcluirArquivo(arquivo_a_excluir)
excluidor.excluir()
