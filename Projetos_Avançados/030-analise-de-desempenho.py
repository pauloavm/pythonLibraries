# Suponha que você deseja criar um script para analisar o desempenho do código Python.

import cProfile

def exemplo_desempenho():
    for _ in range(1000000):
        _ = 1 + 1

if __name__ == "__main__":
    cProfile.run("exemplo_desempenho()")