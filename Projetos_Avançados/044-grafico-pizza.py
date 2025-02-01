import matplotlib.pyplot as plt

def create_pie_chart(data, labels):
    # Cria o gráfico de pizza
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'gray'})

    # Adiciona título
    ax.set_title('Gráfico de Pizza Interativo')

    # Torna o gráfico de pizza interativo
    def on_click(event):
        if event.inaxes == ax:
            wedge, _ = ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'gray'})
            plt.setp(wedge, width=0.4, edgecolor='white')  # Define a largura da "fatia" selecionada
            plt.draw()

    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.show()

if __name__ == "__main__":
    print("Bem-vindo ao Criador de Gráficos de Pizza Interativos!")
    
    # Solicita ao usuário inserir os dados e rótulos para o gráfico de pizza
    data = []
    labels = []
    while True:
        label = input("Digite o rótulo (ou deixe em branco para parar): ").strip()
        if not label:
            break
        value = float(input("Digite o valor correspondente: "))
        labels.append(label)
        data.append(value)

    if len(data) > 0:
        create_pie_chart(data, labels)
    else:
        print("Nenhum dado fornecido. O programa será encerrado.")