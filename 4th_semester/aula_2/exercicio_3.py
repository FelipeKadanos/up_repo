loop = "S"
count = 0

while loop == "S":
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    cidade = input("Digite sua cidade: ")
    count += 1

    loop = input("Cadastrar mais um usuario? (S/N): ").upper()

print("Participantes cadastrados: ", count)