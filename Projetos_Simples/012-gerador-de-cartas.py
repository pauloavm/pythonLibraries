nome_destinatario = input("Digite o nome do destinatário: ")
nome_remetente = input("Digite o seu nome: ")
sentimento = input("Digite um sentimento (por exemplo, 'amor' ou 'amizade'): ")

carta = f"Querido {nome_destinatario},\n\nEscrevo esta carta para expressar o meu {sentimento} por você. Desde que nos conhecemos, minha vida mudou de maneiras maravilhosas. {nome_destinatario}, você é a luz da minha vida e não posso imaginar um dia sem você.\n\nCom {sentimento},\n{nome_remetente}"

print("\nCarta de Amor Gerada:")
print(carta)