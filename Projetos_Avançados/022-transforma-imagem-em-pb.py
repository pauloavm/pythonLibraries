# pip install pillow

from PIL import Image

# Função para transformar imagem em preto e branco
def transformar_em_preto_e_branco(nome_entrada, nome_saida):
    try:
        imagem = Image.open(nome_entrada)
        imagem_preto_branco = imagem.convert("L")  # Converte para preto e branco
        imagem_preto_branco.save(nome_saida)
        
        print(f"A imagem foi transformada em preto e branco e salva como {nome_saida}.")
    except Exception as e:
        print(f"Erro ao transformar imagem em preto e branco: {str(e)}")

if __name__ == "__main__":
    nome_entrada = input("Digite o nome do arquivo de entrada (por exemplo, imagem.jpg): ")
    nome_saida = input("Digite o nome do arquivo de saída (por exemplo, imagem_preto_branco.jpg): ")

    transformar_em_preto_e_branco(nome_entrada, nome_saida)