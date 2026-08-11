for i in range(2, 11, 2): # 1 a 5
    print(i)

print("=" * 40)
print("Introdução ao Python")
print("=" * 40)
# Disciplica de Topicos Especiais

nome = "Carlos"
idade = 21
curso = "Ciência da Computação"

print(nome)
print(idade)
print(curso)
print(type(nome))
print(type(idade))
print(type(curso))

nome = input("Nome: ")
idade = input("Idade: ")
curso = input("Curso: ")

print(type(nome))
print(type(idade))
print(type(curso))

idade = int(input("Idade: ")) # Conversão para Inteiro
print(type(idade))
altura = int(input("Altura: ")) 

# Operadores
print("Soma: ", 10 + 5)
print("Subtração: ", 10 - 5)
print("Divisão: ", 10 / 5)
print("Divisão Inteira: ", 10 // 3)
print("Resto da Divisão: ", 10 % 3)
print("Potência: ", 2 ** 3)

# Operador Relacional
print(idade >= 18)

# Operador Lógico
print(idade >= 18 and curso == "Engenharia da Computação")

# Condicionais 
nome = input("Nome: ")
nome = int(input("Nome: "))

# Condicionais Simples
if idade >= 18:
    print("Incrição autorizada!")

# Condicional Composta
if idade >= 18:
    print("Incrição autorizada!")
else:
    print("Incrição não autorizada!")

# Condicional Encadeada
if idade >= 16:
    print("Incrição não autorizada!")
elif idade < 18:
    print("Incrição necessária!")
else:
    print("Inscrição permitida")

# Laços de Repetição
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

continuar = "S"
while continuar == "S":
    print("\nNovo Cadastro")
    nome = input("Nome: ")
    continuar = input("Nome cadastro? (S/N)").upper()

for i in range(10): # 0 a 9 
    print(i)

for i in range(1, 6): # 1 a 5
    print(i)
    
for i in range(2, 11, 2): # range(início, fim, passo)
    print(i) # 2, 4, 6, 8, 10

nome = "Python"
for letras in nome:
    print(letras)

# Metodos de String

nome = "Linguagem python"

print(nome.upper()) # Maiusculo
print(nome.lower()) # minusculo
print(nome.title()) # Primeira Letra Das Palavras Em Maiusculo
print(nome.capitalize()) # Primeira letra da frase em maiusculo

nome = "      linguagem python   "
print(nome.strip())