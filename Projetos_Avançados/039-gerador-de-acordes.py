import random

def gerar_acorde():
    notas = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    acorde = random.choice(notas)  # Nota raiz
    tipo_acorde = random.choice(['Maior', 'Menor', 'Sétima', 'Sus4'])
    
    if tipo_acorde != 'Sus4':
        terceira = notas[(notas.index(acorde) + 2) % 7]
    else:
        terceira = notas[(notas.index(acorde) + 1) % 7]
    
    quinta = notas[(notas.index(acorde) + 4) % 7]
    
    if tipo_acorde == 'Sétima':
        setima = notas[(notas.index(acorde) + 6) % 7]
        acorde += '7'
    else:
        setima = ''
    
    return f'{acorde}{tipo_acorde} ({acorde}-{terceira}-{quinta}-{setima})'

# Exemplo de uso:
acorde_aleatorio = gerar_acorde()
print(f'Acorde gerado: {acorde_aleatorio}')