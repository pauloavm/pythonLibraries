import pandas as pd  # Dados
import matplotlib.pyplot as plt  # Gráficos
from random import randint
import time

dados = {'Tempo': [], 'Valor': []}
df = pd.DataFrame(data=dados)

# Utilizar o grafico em tempo real
plt.ion()
fig, ax = plt.subplots()


def atualizar():
    df.plot(x='Tempo', y='Valor', ax=ax)
    plt.pause(1)


while True:
    novo_dado = {'Tempo': pd.Timestamp.now(), 'Valor': randint(0, 100)}
    df = df.append(novo_dado, ignore_index=True)
    atualizar()
    time.sleep(10)