import barcode
from barcode import generate

def gerar_codigo_de_barras(dados, formato):
    try:
        codigo = barcode.get(formato, dados)
        codigo.save(f'codigo_de_barras_{dados}')
        print(f'Código de barras gerado com sucesso: codigo_de_barras_{dados}.{formato}')
    except Exception as e:
        print(f"Erro ao gerar código de barras: {str(e)}")

if __name__ == "__main__":
    dados = input("Digite os dados para o código de barras: ")
    formato = input("Digite o formato desejado (E.g., 'EAN13', 'CODE128'): ")
    gerar_codigo_de_barras(dados, formato)