import sys

class GerenciadorContextoSys:
    def __init__(self):
        pass

    def __enter__(self):
        print("Entrando no contexto")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Saindo do contexto")
        if exc_type:
            print("Ocorreu uma exceção:", exc_type)

with GerenciadorContextoSys() as contexto:
    print("Dentro do contexto")
    # Adicione código que pode lançar exceções para testar a funcionalidade de saída do contexto
    # raise ValueError("Exemplo de exceção")
