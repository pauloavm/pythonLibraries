from datetime import datetime

class DiaSemanaData:
    def __init__(self, data):
        self.data = datetime.strptime(data, "%Y-%m-%d")

    def obter_dia_semana(self):
        dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        return dias_semana[self.data.weekday()]

data = "2024-03-12"
dia_semana = DiaSemanaData(data)
print("Dia da semana para", data, ":", dia_semana.obter_dia_semana())
