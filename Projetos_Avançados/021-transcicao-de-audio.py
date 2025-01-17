from google.cloud import speech_v1p1beta1 as speech
import io

# Configure as credenciais do Google Cloud
# Certifique-se de ter as credenciais JSON do serviço configuradas como variável de ambiente

def transcrever_audio(arquivo_audio):
    client = speech.SpeechClient()

    with io.open(arquivo_audio, "rb") as audio_file:
        conteudo_audio = audio_file.read()

    audio = speech.RecognitionAudio(content=conteudo_audio)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="pt-BR",  # Idioma do áudio (por exemplo, pt-BR para português)
    )

    response = client.recognize(config=config, audio=audio)

    # Exibindo as transcrições
    for resultado in response.results:
        print(f"Transcrição: {resultado.alternatives[0].transcript}")

if __name__ == "__main__":
    arquivo_audio = input("Digite o caminho para o arquivo de áudio a ser transcrita: ")
    transcrever_audio(arquivo_audio)