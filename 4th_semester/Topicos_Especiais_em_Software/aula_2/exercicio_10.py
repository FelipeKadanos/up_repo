total = 0
soma_idade = 0
est = 0
prof = 0
palestrantes = 0
maior_idade = 0
manor_idade = 0
mais_velho = ""
mais_novo = ""
loop = "S"

while loop == "S":
    nome = input("Digite o nome:")
    idade = int(input("Digite a idade: "))
    cidade = input("Digite a cidade: ")
    categoria = input("Digite a categoria: ").upper()

    while categoria != "ESTUDANTE" and categoria != "PROFISSIONAL" and categoria != "PALESTRANTE":
        print("Categoria invalida!")
        categoria = input("Digite a categoria novamente: ").upper()

    totla += 1
    soma_idade += idade

    if cat == "ESTUDANTE":
        est += 1
    elif cat == "PROFISSIONAL":
        prof += 1
    else:
        palestrantes += 1

    if total == 1:
        maior_idade = idade
        menor_idade = idade
        mais_velho = nome
        mais_novo = nome
    else:
        if idade > maior_idade:
            maior_idade = idade
            mais_velho = nome
        if idade < menor_idade:
            menor_idade = idade
            mais_novo = nome

    loop = input("Continuar cadastrando participantes? (S/N): ").upper()

media = soma_idade / total

print(f"Total de participantes: {total}")
print(f"Total de estudantes: {est}")
print(f"Total de profissionais: {prof}")
print(f"Total de palestrantes: {palestrantes}")
print(f"Nome e idade do participantes mais velhor: {mais_velho} {maior_idade} anos")
print(f"Nome e idade do participantes mais novo: {mais_novo} {menor_idade} anos")
print(f"Media de idade dos participantes: {media}")