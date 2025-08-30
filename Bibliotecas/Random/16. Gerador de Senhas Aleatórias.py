import random
import string


class GeradorSenha:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def gerar_senha(self):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = "".join(random.choice(caracteres) for i in range(self.tamanho))
        return senha


gerador = GeradorSenha(12)
print("Senha Aleatória:", gerador.gerar_senha())
