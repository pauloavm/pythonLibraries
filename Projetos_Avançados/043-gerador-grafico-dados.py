'''Esse código se trada de um projeto para criar gráficos, então você vai precisar 
com os valores que ele vai trabalhar.

'''
import matplotlib.pyplot as plt

def generate_bar_chart(data, labels, title):
    plt.figure(figsize=(10, 6))  # Define o tamanho da figura

    # Cria o gráfico de barras
    plt.bar(labels, data, color='royalblue')

    # Adiciona rótulos ao eixo x, eixo y e título
    plt.xlabel('Categorias')
    plt.ylabel('Valores')
    plt.title(title)

    # Exibe o gráfico
    plt.show()

if __name__ == "__main__":
    # Dados de exemplo (substitua pelos seus próprios dados)
    categories = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D']
    values = [25, 40, 30, 60]
    chart_title = 'Gráfico de Barras de Exemplo'

    generate_bar_chart(values, categories, chart_title)