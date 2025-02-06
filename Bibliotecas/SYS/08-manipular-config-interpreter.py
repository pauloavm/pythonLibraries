import sys

class ConfiguracaoInterpretador:
    def __init__(self):
        pass

    def alterar_variavel_interpretador(self, variavel, valor):
        setattr(sys, variavel, valor)

config_interpretador = ConfiguracaoInterpretador()
config_interpretador.alterar_variavel_interpretador("maxsize", 99999)
print("Tamanho máximo de um objeto:", sys.maxsize)
