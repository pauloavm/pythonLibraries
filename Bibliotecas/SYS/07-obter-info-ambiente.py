import sys

class InformacoesAmbientePython:
    def __init__(self):
        pass

    def obter_info_ambiente(self):
        print("Versão do Python:", sys.version)
        print("Plataforma:", sys.platform)
        print("Prefixo do Executável:", sys.exec_prefix)
        print("Caminho do Módulo:", sys.path)

info_ambiente = InformacoesAmbientePython()
info_ambiente.obter_info_ambiente()
