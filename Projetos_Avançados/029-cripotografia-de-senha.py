# Suponha que você deseja criar um gerenciador de senhas criptografadas em Python.
# pip install cryptography-fernet

from cryptography.fernet import Fernet

# Chave secreta para criptografar/descriptografar senhas
chave_secreta = Fernet.generate_key()
fernet = Fernet(chave_secreta)

def criptografar_senha(senha):
    return fernet.encrypt(senha.encode()).decode()

def descriptografar_senha(senha_criptografada):
    return fernet.decrypt(senha_criptografada.encode()).decode()

senha_original = "MinhaSenhaSecreta"
senha_criptografada = criptografar_senha(senha_original)
senha_descriptografada = descriptografar_senha(senha_criptografada)

print(f"Senha Original: {senha_original}")
print(f"Senha Criptografada: {senha_criptografada}")
print(f"Senha Descriptografada: {senha_descriptografada}")