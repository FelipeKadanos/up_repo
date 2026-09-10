# NUMPY

# NumPy significa Numerical Python.
# E uma biblioteca usada para arrays, matrizes e calculos numericos.
# Instalacao:
# pip install numpy

import numpy as np


# CRIANDO O PRIMEIRO ARRAY
numeros = np.array([10, 20, 30, 40, 50])
print(numeros)


# LISTA PYTHON X ARRAY NUMPY
lista = [10, 20, 30, 40]
print(lista * 2)  # repete os elementos

numeros = np.array([10, 20, 30, 40])
print(numeros * 2)  # multiplica cada elemento


# OPERACOES COM ARRAYS
print(numeros + 5)
print(numeros - 5)
print(numeros * 2)
print(numeros / 2)


# OPERACOES ENTRE DOIS ARRAYS
a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# ACESSANDO E ALTERANDO ELEMENTOS
numeros = np.array([10, 20, 30, 40, 50])
print(numeros[0])
print(numeros[2])

numeros[0] = 100
print(numeros)


# FATIAMENTO DE ARRAYS
print(numeros[1:4])
print(numeros[:3])
print(numeros[2:])


# PROPRIEDADES IMPORTANTES
print(numeros.ndim)   # numero de dimensoes
print(numeros.shape)  # formato
print(numeros.size)   # quantidade de elementos
print(numeros.dtype)  # tipo dos elementos


# FUNCOES MATEMATICAS
notas = np.array([7.5, 8.0, 6.5, 9.0, 8.5])

print(np.sum(notas))
print(np.mean(notas))
print(np.max(notas))
print(np.min(notas))


# COMPARACOES E INDEXACAO BOOLEANA
notas = np.array([5.0, 8.0, 4.5, 9.0, 7.5])
print(notas >= 7)

aprovados = notas[notas >= 7]
print(aprovados)


# MATRIZES
matriz = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
])

print(matriz)
print(matriz[1, 2])  # linha 1, coluna 2 -> 60


# CRIANDO ARRAYS AUTOMATICAMENTE
zeros = np.zeros(5)
uns = np.ones(5)
sequencia = np.arange(1, 11)

print(zeros)
print(uns)
print(sequencia)
