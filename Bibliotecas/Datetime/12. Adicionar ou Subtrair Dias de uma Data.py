from datetime import datetime, timedelta

class OperacoesData:
    def __init__(self, data, dias):
        self.data = datetime.strptime(data, "%Y-%m-%d")
        self.dias = dias

    def adicionar_dias(self):
        nova_data = self.data + timedelta(days=self.dias)
        return nova_data.strftime("%Y-%m-%d")

data_atual = "2024-03-12"
dias_para_adicionar = 7
operacoes = OperacoesData(data_atual, dias_para_adicionar)
print("Nova data após adicionar", dias_para_adicionar, "dias:", operacoes.adicionar_dias())
