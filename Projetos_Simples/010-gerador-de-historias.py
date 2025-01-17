import random

# Listas de elementos para a história
personagens = ["Alice", "Bob", "Charlie", "David", "Eva", "Fernanda"]
lugares = ["uma cidade pequena", "uma floresta mágica", "um castelo antigo", "uma ilha deserta", "um planeta distante"]
eventos = ["encontrou um mapa do tesouro", "descobriu um portal misterioso", "foi em uma aventura incrível", "fez um amigo inesperado"]
desfechos = ["eles viveram felizes para sempre.", "eles aprenderam uma valiosa lição.", "eles encontraram o que estavam procurando."]

# Função para gerar uma história aleatória
def gerar_historia():
    personagem = random.choice(personagens)
    lugar = random.choice(lugares)
    evento = random.choice(eventos)
    desfecho = random.choice(desfechos)

    historia = f"{personagem} estava em {lugar} quando {evento}. No final, {desfecho}"

    return historia

# Gerar e exibir a história
historia_gerada = gerar_historia()
print("História Gerada:")
print(historia_gerada)