import sys

class ExcecaoNaoTratada:
    def __init__(self):
        pass

    def excecao_nao_tratada(self, exc_type, exc_value, exc_traceback):
        print("Ocorreu uma exceção não tratada:")
        print("Tipo:", exc_type)
        print("Valor:", exc_value)
        print("Rastreamento:", exc_traceback)

    def ativar_monitoramento_excecoes(self):
        sys.excepthook = self.excecao_nao_tratada

excecao_monitor = ExcecaoNaoTratada()
excecao_monitor.ativar_monitoramento_excecoes()

# Aqui você pode adicionar código que gera uma exceção não tratada para testar a funcionalidade
# raise ValueError("Exemplo de exceção não tratada")
