loop = "S"
count = 0
soma = 0
maiores = 0
menores = 0

while loop == "S":
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    cidade = input("Digite sua cidade: ")
    count += 1
    soma +=idade
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

    loop = input("Cadastrar mais um usuario? (S/N): ").upper()

media = soma / count

print("Participantes cadastrados: ", count)
print(f"Maiores de idade: {maiores}")
print(f"Menores de idade: {menores}")
print(f"Media das idade: {media}")