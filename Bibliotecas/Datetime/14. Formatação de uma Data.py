from datetime import datetime

class FormatacaoData:
    def __init__(self, data):
        self.data = datetime.strptime(data, "%Y-%m-%d")

    def formatar_data(self, formato):
        return self.data.strftime(formato)

data = "2024-03-12"
formatador = FormatacaoData(data)
print("Data formatada (DD/MM/AAAA):", formatador.formatar_data("%d/%m/%Y"))
