#Função
def soma(a, b):
    return a + b

resultado = soma(10, 20)
print(resultado)


# Funções Recursiva

def contagem(numero):
    if numero == 0:
        return
    print(numero)
    contagem(numero - 1)

contagem(5)