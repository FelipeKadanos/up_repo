count = 0

while True:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    if idade == 0:
        break
    
    if idade < 0:
        print("Erro! A idade não pode ser negativa.")
        continue

    count += 1

print(f"\nQuantidade de participantes validos: {count}")