import subprocess


def compilar(caminho_arquivo):
    try:
        comando = f'g++ {caminho_arquivo} -o programa'
        subprocess.run(comando, shell=True, check=True)
        print('Compilação bem-sucedida')
    except subprocess.CalledProcessError:
        print('Erro na compilação')


if __name__ == '__main__':
    arquivo = ''  # Caminho do arquivo
    compilar(arquivo)