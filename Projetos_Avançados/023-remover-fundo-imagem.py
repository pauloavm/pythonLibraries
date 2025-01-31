# pip install rembg
# pip install requests

import requests
from rembg import remove

# Função para remover o fundo de uma imagem
def remover_fundo_imagem(imagem_url, nome_saida):
    try:
        img = requests.get(imagem_url).content
        img_sem_fundo = remove(img)
        
        # Salvar a imagem sem fundo
        with open(nome_saida, 'wb') as arquivo_saida:
            arquivo_saida.write(img_sem_fundo)
        
        print(f"O fundo da imagem foi removido com sucesso e salvo como {nome_saida}.")
    except Exception as e:
        print(f"Erro ao remover fundo da imagem: {str(e)}")

if __name__ == "__main__":
    imagem_url = input("Digite a URL da imagem que deseja processar: ")
    nome_saida = input("Digite o nome do arquivo de saída (por exemplo, imagem_sem_fundo.png): ")

    remover_fundo_imagem(imagem_url, nome_saida)