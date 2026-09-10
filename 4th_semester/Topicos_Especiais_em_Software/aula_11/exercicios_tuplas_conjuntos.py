# EXERCICIOS - TUPLAS, CONJUNTOS, ENUMERATE E ZIP


# 1. Crie uma tupla com cinco cidades. Mostre todas as cidades e depois
# exiba a primeira e a ultima.
cidades = ("Curitiba", "Londrina", "Maringa", "Cascavel", "Ponta Grossa")

print("Exercicio 1")
for cidade in cidades:
    print(cidade)

print("Primeira:", cidades[0])
print("Ultima:", cidades[-1])


# 2. Crie uma tupla com nome, idade e curso de um aluno.
# Utilize desempacotamento para armazenar os valores em tres variaveis.
print("\nExercicio 2")
aluno = ("Ana", 20, "Engenharia")
nome, idade, curso = aluno

print("Nome:", nome)
print("Idade:", idade)
print("Curso:", curso)


# 3. Leia 10 numeros, armazene-os em uma lista e utilize um conjunto para
# mostrar apenas os valores diferentes.
print("\nExercicio 3")
numeros = [10, 20, 10, 30, 40, 20, 50, 60, 50, 70]
numeros_diferentes = set(numeros)

print("Numeros informados:", numeros)
print("Numeros diferentes:", numeros_diferentes)


# 4. Crie dois conjuntos com nomes de alunos de duas disciplinas.
# Mostre os alunos que estao nas duas disciplinas e todos sem repeticao.
print("\nExercicio 4")
python = {"Ana", "Carlos", "Pedro", "Mariana"}
banco_de_dados = {"Carlos", "Mariana", "Joao", "Bianca"}

print("Nas duas disciplinas:", python & banco_de_dados)
print("Todos os alunos:", python | banco_de_dados)


# 5. Crie uma lista com cinco produtos. Utilize enumerate() para exibir
# a numeracao e o nome de cada produto.
print("\nExercicio 5")
produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Webcam"]

for indice, produto in enumerate(produtos, start=1):
    print(indice, "-", produto)


# 6. Crie uma lista com nomes de cinco alunos e outra com suas notas.
# Utilize zip() para mostrar nome e nota de cada aluno.
print("\nExercicio 6")
alunos = ["Ana", "Carlos", "Pedro", "Mariana", "Joao"]
notas = [8.5, 7.0, 9.0, 6.5, 8.0]

for aluno, nota in zip(alunos, notas):
    print(aluno, "-", nota)


# 7. Desafio: a partir de duas listas contendo alunos inscritos em dois cursos,
# mostre alunos unicos, alunos presentes nos dois cursos e alunos exclusivos
# do primeiro curso.
print("\nExercicio 7")
curso_python = ["Ana", "Carlos", "Pedro", "Mariana", "Ana"]
curso_java = ["Carlos", "Bianca", "Mariana", "Joao"]

set_python = set(curso_python)
set_java = set(curso_java)

print("Alunos unicos:", set_python | set_java)
print("Nos dois cursos:", set_python & set_java)
print("Exclusivos do primeiro curso:", set_python - set_java)
