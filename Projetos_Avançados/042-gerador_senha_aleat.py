import string
import secrets

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Crie uma lista de caracteres com base nas opções selecionadas
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Selecione pelo menos um tipo de caractere.")
        return None

    # Gere uma senha aleatória usando a biblioteca secrets
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Senhas Aleatórias!")
    while True:
        length = int(input("Digite o comprimento da senha desejada: "))
        use_lowercase = input("Incluir letras minúsculas? (Sim/Não): ").strip().lower() == "sim"
        use_uppercase = input("Incluir letras maiúsculas? (Sim/Não): ").strip().lower() == "sim"
        use_digits = input("Incluir dígitos? (Sim/Não): ").strip().lower() == "sim"
        use_special_chars = input("Incluir caracteres especiais? (Sim/Não): ").strip().lower() == "sim"

        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)

        if password:
            print(f'Sua senha gerada é: {password}')

        another = input("Deseja gerar outra senha? (Sim/Não): ").strip().lower()
        if another != "sim":
            break