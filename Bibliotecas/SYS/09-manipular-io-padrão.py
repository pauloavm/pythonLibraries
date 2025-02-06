import sys

class ManipulacaoEntradaSaida:
    def __init__(self):
        pass

    def ler_linhas_entrada_padrao(self):
        for linha in sys.stdin:
            print("Entrada Padrão:", linha)

    def redirecionar_saida_padrao(self):
        sys.stdout = open('saida.txt', 'w')
        print("Este é um teste de saída padrão redirecionada.")
        sys.stdout.close()

manipulador_io = ManipulacaoEntradaSaida()
manipulador_io.ler_linhas_entrada_padrao()
manipulador_io.redirecionar_saida_padrao()
