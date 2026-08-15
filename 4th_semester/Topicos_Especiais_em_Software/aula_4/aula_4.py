# LISTA:

# Lista vazia:
nomes = []

# Lista numérica:
idades = [20,18,25,30]

# Lista misturada:
dados = ["Carlos", 20, 1.80, True] # não é uma boa prática

# Lista preenchida:
nomes = ["Carlos", "Ana", "Pedro"]

# Acessando as posições:
print(nomes[0])
print(nomes[1])
print(nomes[2])

nomes = ["Carlos", "Ana", "Pedro"]
nomes[1] = "Maria"
print(nomes) # ["Carlos", "Maria", "Pedro"]

# Como colocar um quarto participante?
nomes.append("José")
print(nomes) # ["Carlos", "Maria", "Pedro", "José"]  |  append() adiciona sempre ao final.

# PERCORRENDO LISTAS

# Primeira maneira:
for nome in nomes:
    print(nome)

# Segunda maneira:
for i in range(len(nomes)):
    print(nomes[i])

# REMOVE()
nomes.remove("Carlos") # Remove pelo conteudo

# POP()
nomes.pop() # Remove o último
nomes.pop(1) # Remove pela posição

# IN
if "Carlos" in nomes:
    print("Encontrado") # Muito utilizado para pesquisas

# SORT()
nomes.sort() # Coloca a lista em ordem alfabética
nomes.sort(reverse=True) # Coloca em ordem alfabética em ordem invertida

# REVERSE()
nomes.reverse() # Inverte a ordem da lista

# CLEAR()
nomes.clear() # Apaga todos os elementos