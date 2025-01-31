from datetime import date

def calcular_idade(data_nascimento):
    hoje = date.today()
    ano_nascimento = data_nascimento.year
    idade = hoje.year - ano_nascimento
    if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
        idade -= 1
    return idade

data_nascimento = date(2000, 1, 1)  # Substitua com a data de nascimento do usuário
idade = calcular_idade(data_nascimento)
print(f'Sua idade é: {idade} anos')