import plotly.express as px
import pandas as pd

# Função para criar um gráfico de barras interativo
def criar_grafico_de_barras(dados, x_coluna, y_coluna, titulo):
    fig = px.bar(dados, x=x_coluna, y=y_coluna, title=titulo)
    fig.show()

# Função para criar um gráfico de dispersão interativo
def criar_grafico_de_dispersao(dados, x_coluna, y_coluna, titulo):
    fig = px.scatter(dados, x=x_coluna, y=y_coluna, title=titulo)
    fig.show()

# Função para criar um gráfico de pizza interativo
def criar_grafico_de_pizza(dados, labels_coluna, valores_coluna, titulo):
    fig = px.pie(dados, names=labels_coluna, values=valores_coluna, title=titulo)
    fig.show()

# Exemplo de uso das funções
if __name__ == "__main__":
    # Suponha que você tenha um DataFrame de exemplo com dados
    dados = pd.DataFrame({
        'Categoria': ['A', 'B', 'C', 'D'],
        'Valores': [10, 30, 15, 25]
    })

    # Criar um gráfico de barras
    criar_grafico_de_barras(dados, 'Categoria', 'Valores', 'Gráfico de Barras Interativo')

    # Criar um gráfico de dispersão
    criar_grafico_de_dispersao(dados, 'Categoria', 'Valores', 'Gráfico de Dispersão Interativo')

    # Criar um gráfico de pizza
    criar_grafico_de_pizza(dados, 'Categoria', 'Valores', 'Gráfico de Pizza Interativo')