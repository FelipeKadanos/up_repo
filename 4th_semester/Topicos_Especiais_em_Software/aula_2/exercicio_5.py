count = 0
nota_alta = 0
maior = 0
menor = 10


for i in range(10):
    print("Digite a nota do aluno ", i + 1)
    nota = float(input("Digite a nota: "))
    soma_nota += nota

    if nota > maior_nota:
        maior = nota
    if nota < menor_nota:
        menor = nota
    if nota >= 8:
        nota_alta += 1

media = soma_notas / 10

print("Participantes cadastrados: ", count)
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Media das notas: {media}")