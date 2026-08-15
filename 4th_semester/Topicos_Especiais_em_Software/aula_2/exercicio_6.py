usuario_correto = "ADMIN"
senha_correta = "123"

while tentativas <= 3:
    usuario = input("Digite o usuario: ").upper()
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo ao sistema.")
        break
    else:
        tentativas += 1
        print("Usuario ou senha incorretos!")

if tentativas == 3:
    print("Usuario bloqueado!")