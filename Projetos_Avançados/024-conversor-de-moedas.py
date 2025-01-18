import requests

# Chave da API do ExchangeRatesAPI.io (obtenha a sua em https://exchangeratesapi.io/)
API_KEY = 'SUA_CHAVE_DA_API'

def obter_taxas_de_cambio(base_currency):
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={base_currency}&apikey={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates']
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter taxas de câmbio: {e}")
        return None

def converter_moeda(valor, de_moeda, para_moeda):
    taxas = obter_taxas_de_cambio(de_moeda)
    
    if taxas:
        if para_moeda in taxas:
            taxa_de_cambio = taxas[para_moeda]
            resultado = valor * taxa_de_cambio
            return resultado
        else:
            print(f"A moeda de destino '{para_moeda}' não está disponível.")
    else:
        print("Não foi possível obter as taxas de câmbio.")

if __name__ == "__main__":
    print("Bem-vindo ao Conversor de Moedas Avançado!")
    valor = float(input("Digite o valor a ser convertido: "))
    moeda_origem = input("Digite a moeda de origem (por exemplo, USD, EUR): ").upper()
    moeda_destino = input("Digite a moeda de destino (por exemplo, GBP, JPY): ").upper()

    resultado = converter_moeda(valor, moeda_origem, moeda_destino)

    if resultado is not None:
        print(f"{valor} {moeda_origem} equivale a {resultado:.2f} {moeda_destino}")