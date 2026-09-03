from livro import Livro
from dados import livros


def cadastrar():

    print("\n===== CADASTRO DE LIVRO =====")

    titulo = input("Título: ").strip().title()
    autor = input("Autor: ").strip().title()
    editora = input("Editora: ").strip().title()

    try:
        ano = int(input("Ano: "))
        preco = float(input("Preço: R$ "))
    except ValueError:
        print("\nAno ou preço inválido.")
        return

    if ano <= 0:
        print("\nAno inválido.")
        return

    if preco < 0:
        print("\nPreço inválido.")
        return

    livro = Livro(
        titulo,
        autor,
        ano,
        editora,
        preco
    )

    livros.append(livro)
    print("\nLivro cadastrado com sucesso!")

def listar():
    if len(livros) == 0:
        print("\nNenhum livro cadastrado.")
        return

    print("\n========== LIVROS ==========")

    for livro in livros:
        livro.mostrar_dados()


def procurar():
    if len(livros) == 0:
        print("\nNenhum livro cadastrado.")
        return

    titulo = input("\nTítulo do livro: ").strip().title()
    encontrado = False

    for livro in livros:
        if livro.titulo == titulo:
            print("\nLivro encontrado!")
            livro.mostrar_dados()
            encontrado = True
            break

    if not encontrado:
        print("\nLivro não encontrado.")

def alterar():
    titulo = input("\nTítulo do livro: ").strip().title()
    encontrado = False

    for livro in livros:
        if livro.titulo == titulo:
            encontrado = True
            print("\nLivro encontrado.")
            livro.mostrar_dados()

            try:
                novo_ano = int(input("\nNovo ano: "))
                novo_preco = float(input("Novo preço: R$ "))

            except ValueError:
                print("\nDigite valores numéricos.")
                return

            livro.ano = novo_ano
            livro.preco = novo_preco
            print("\nAlteração concluída.")
            break

    if not encontrado:
        print("\nLivro não encontrado.")

def excluir():
    titulo = input("\nTítulo do livro: ").strip().title()
    encontrado = False

    for livro in livros:
        if livro.titulo == titulo:
            livros.remove(livro)
            print("\nLivro excluído com sucesso.")
            encontrado = True
            break

    if not encontrado:
        print("\nLivro não encontrado.")


def estatisticas():
    if len(livros) == 0:
        print("\nNenhum livro cadastrado.")
        return

    total_livros = len(livros)
    soma_precos = 0
    livro_mais_caro = livros[0]
    livro_mais_barato = livros[0]

    for livro in livros:
        soma_precos += livro.preco

        if livro.preco > livro_mais_caro.preco:
            livro_mais_caro = livro

        if livro.preco < livro_mais_barato.preco:
            livro_mais_barato = livro

    media_precos = soma_precos / total_livros

    print("\n========== ESTATÍSTICAS ==========")
    print("Quantidade de livros:", total_livros)
    print("Valor total: R$",round(soma_precos, 2))
    print("Preço médio: R$",round(media_precos, 2))
    print("\nLivro mais caro:",livro_mais_caro.titulo)
    print("Preço: R$",livro_mais_caro.preco)
    print("\nLivro mais barato:",livro_mais_barato.titulo)
    print("Preço: R$",livro_mais_barato.preco)
