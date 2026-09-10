# EXERCICIO - SISTEMA DE ANALISE DE NOTAS COM NUMPY

import numpy as np


notas = np.array([7.5, 8.0, 5.5, 9.0, 6.0, 8.5, 4.0, 7.0])

print("Todas as notas:", notas)
print("Quantidade de notas:", notas.size)
print("Maior nota:", np.max(notas))
print("Menor nota:", np.min(notas))
print("Media da turma:", np.mean(notas))

notas_aprovadas = notas[notas >= 7]
notas_abaixo_7 = notas[notas < 7]

print("Notas maiores ou iguais a 7:", notas_aprovadas)
print("Quantidade de alunos com nota maior ou igual a 7:", notas_aprovadas.size)
print("Notas abaixo de 7:", notas_abaixo_7)
