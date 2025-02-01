def calcular_tempo_de_viagem(distancia, velocidade_media):
    # Calcula o tempo de viagem em horas
    tempo_em_horas = distancia / velocidade_media
    return tempo_em_horas

if __name__ == "__main__":
    print("Bem-vindo à Calculadora de Tempo de Viagem!")

    try:
        distancia = float(input("Digite a distância da viagem (em quilômetros): "))
        velocidade_media = float(input("Digite a velocidade média (em km/h): "))

        tempo_em_horas = calcular_tempo_de_viagem(distancia, velocidade_media)

        # Converte o tempo de horas para minutos
        tempo_em_minutos = tempo_em_horas * 60

        print(f"Tempo estimado de viagem: {tempo_em_horas:.2f} horas ({tempo_em_minutos:.2f} minutos)")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números válidos para a distância e a velocidade média.")