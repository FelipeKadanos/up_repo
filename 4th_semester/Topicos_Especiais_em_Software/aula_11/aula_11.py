# TUPLAS, CONJUNTOS, ENUMERATE E ZIP

# ESTRUTURAS DE DADOS
# lista = [10, 20, 30]      -> ordenada e mutavel
# tupla = (10, 20, 30)      -> ordenada e imutavel
# conjunto = {10, 20, 30}   -> nao armazena valores repetidos


# TUPLAS
# Tuplas guardam varios valores em uma estrutura unica.
# Elas mantem a ordem, permitem acesso por indice e nao podem ser alteradas.
cores = ("azul", "verde", "vermelho")
print(cores)
print(cores[0])
print(cores[2])

# cores[0] = "amarelo"  # Erro: tuplas sao imutaveis.


# PERCORRENDO UMA TUPLA
cidades = ("Curitiba", "Londrina", "Maringa")

for cidade in cidades:
    print(cidade)


# DESEMPACOTAMENTO DE TUPLAS
dados = ("Carlos", 22, "Curitiba")
nome, idade, cidade = dados

print(nome)
print(idade)
print(cidade)


# CONJUNTOS - SET
# Conjuntos nao aceitam duplicidade e nao sao acessados por posicao.
numeros = {10, 20, 30, 20, 10}
print(numeros)

linguagens = {"Python", "Java", "C"}
linguagens.add("JavaScript")
print(linguagens)

linguagens.remove("C")
print(linguagens)


# ELIMINANDO VALORES DUPLICADOS
nomes = ["Ana", "Carlos", "Ana", "Pedro", "Carlos"]
nomes_sem_repeticao = set(nomes)
print(nomes_sem_repeticao)


# OPERACOES ENTRE CONJUNTOS
turma_a = {"Ana", "Carlos", "Pedro"}
turma_b = {"Carlos", "Mariana", "Pedro"}

print(turma_a | turma_b)  # uniao
print(turma_a & turma_b)  # intersecao
print(turma_a - turma_b)  # diferenca


# ENUMERATE()
# Retorna indice e valor ao mesmo tempo.
cidades = ["Curitiba", "Londrina", "Maringa"]

for indice, cidade in enumerate(cidades):
    print(indice, cidade)


# ZIP()
# Percorre duas ou mais colecoes em paralelo.
nomes = ["Ana", "Carlos", "Pedro"]
notas = [8.5, 7.0, 9.0]

for nome, nota in zip(nomes, notas):
    print(nome, "-", nota)
