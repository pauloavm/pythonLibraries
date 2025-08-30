from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

# URL corrigida, sem espaços extras
url = "https://www.youtube.com/watch?v=_hHzhijt-Jk"

# Define a pasta de destino para os vídeos baixados
destino = Path("pasta_video_DL")
# Cria a pasta se ela não existir
destino.mkdir(exist_ok=True)

try:
    # Inicializa o objeto YouTube com a URL e a função de callback de progresso
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"Titulo: {yt.title}\nDuracao: {yt.length}s")

    # Obtém o stream com a maior resolução disponível
    stream = yt.streams.get_highest_resolution()

    # Verifica se um stream foi encontrado
    if stream is not None:
        # Se encontrou, inicia o download para a pasta de destino
        print("Iniciando o download...")
        stream.download(output_path=str(destino))
        print(f"Download concluído! Vídeo salvo em: {destino}")
    else:
        # Informa caso nenhum stream de alta resolução seja encontrado
        print("Nenhum stream de alta resolução encontrado para este vídeo.")

except Exception as e:
    # Captura e exibe outras exceções que possam ocorrer
    print(f"Ocorreu um erro: {e}")
