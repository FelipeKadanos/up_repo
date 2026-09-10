# FUNCOES LAMBDA

# Lambda e uma funcao pequena escrita em uma unica expressao.
# Ela e muito util quando precisamos passar uma funcao para outra operacao.


# FUNCAO TRADICIONAL X LAMBDA
def dobro_tradicional(numero):
    return numero * 2


dobro = lambda numero: numero * 2

print(dobro_tradicional(5))
print(dobro(5))


# ESTRUTURA
# lambda parametros: expressao
# Nao usamos return: o resultado da expressao e retornado automaticamente.
somar = lambda a, b: a + b
multiplicar = lambda a, b: a * b

print(somar(10, 5))
print(multiplicar(4, 5))


# LAMBDA COM MAX()
class Livro:
    def __init__(self, titulo, preco):
        self.titulo = titulo
        self.preco = preco


livros = [
    Livro("Python", 80),
    Livro("Banco de Dados", 120),
    Livro("Redes", 95),
]

mais_caro = max(livros, key=lambda livro: livro.preco)
print(mais_caro.titulo)


# LAMBDA COM SORTED()
alunos = [
    ("Carlos", 7.5),
    ("Ana", 9.0),
    ("Pedro", 6.5),
]

ordenados = sorted(alunos, key=lambda aluno: aluno[1])
print(ordenados)

ordenados_decrescente = sorted(alunos, key=lambda aluno: aluno[1], reverse=True)
print(ordenados_decrescente)


# LAMBDA COM MAP()
numeros = [1, 2, 3, 4, 5]
dobros = map(lambda numero: numero * 2, numeros)
print(list(dobros))


# LAMBDA COM FILTER()
idades = [15, 22, 17, 30, 16, 25]
maiores = filter(lambda idade: idade >= 18, idades)
print(list(maiores))
