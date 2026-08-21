# PRINCIPAIS EXCEÇÕES
# Exceção                Quando ocorre

# ValueError             Conversão inválida (int, float)
# ZeroDivisionError      Divisão por zero
# FileNotFoundError      Arquivo inexistente
# IndexError             Índice inválido em listas
# KeyError               Chave inexistente em dicionários

# EXCEPITONS
try:
    idade = int(input("Idade: "))
    print(f"Idade: {idade}")
except:
    print("Valor inválido.")

# Try: Tente executar.
# Exception: Caso ocorra um erro, execute este bloco

# ERROS ESPECÍFICOS
try:
    idade = int(input("Idade: "))
except ValueError:
    print("Digite apenas números.")

# ELSE
try:
    idade = int(input("Idade: "))
except ValueError:
    print("Valor inválido.")
else: #Executado somente quando não ocorre erro
    print("Cadastro realizado.")

# FINALLY
try:
    idade = int(input("Idade: "))
except ValueError:
    print("Valor inválido.")
finally: #Sempre será executado
    print("Fim do programa.")

# EXEMPLO COM DIVISÃO
try:
    numero = int(input("Número: "))
    resultado = 100 / numero
    print(resultado)
except ZeroDivisionError:
    print("Não existe divisão por zero.")
except ValueError:
    print("Digite apenas números.")

# EXEMPLO COM ARQUIVOS
try:
    with open("alunos.txt","r") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Arquivo não encontrado.")


