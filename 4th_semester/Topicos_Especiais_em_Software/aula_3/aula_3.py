# OPERADORES DE PERTENCIMENTO

texto = "Python"
print = ("P" in texto) #Verifica se a letra P está no texto.
#Retorna um valor Booleano.
print = ("z" not in texto) #Verifica se a letra z não está no texto.

# funções Built-in
texto = “Palavra”
# len()
print(len(texto)) #Retorna o tamanho de uma string

# max()
print(max(10,20,30)) # Retorna o valor maior

# min()
print(min(10,20,30)) # Retorna o valor menor

# round() 
media = 2.5
print(round(media, 2))  # Arredondamento

# abs()
print(abs(-50)) # Valor absoluto

# MATCH CASE 
opcao = int(input("Digite um numero de 1 a 3: "))

match opcao:
    case 1:
        print("Opcao 1")

    case 2: 
        print("Opcao 2")

    case 3:
        print("Opcao 3")

    case _:
        print("Opcao invalida")

# AVANÇAR UM BLOCO DE CODIGO
if idade >= 18
    pass
else:
    print("Menor.")

# REPLACE
texto = "Python"
print(texto.replace("Python","Java"))

# COUNT
texto = "Banana"
print(texto.count("a")) # Retorna 3

# FIND
texto = "Universidade"
print(texto.find("vers")) # Retona 3, se não encontrar retorna -1

# SPLIT
texto = "Python Java JavaScript"
print(texto.split()) # [‘Python’, ‘Java’, ‘JavaScript’]