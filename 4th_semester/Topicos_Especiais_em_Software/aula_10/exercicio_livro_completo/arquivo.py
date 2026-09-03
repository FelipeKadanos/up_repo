from dados import livros
from livro import Livro


def salvar():

    try:
        with open("livros.txt", "w") as arquivo:
            for livro in livros:
                linha = (
                    livro.titulo + ";" +
                    livro.autor + ";" +
                    str(livro.ano) + ";" +
                    livro.editora + ";" +
                    str(livro.preco) + "\n"
                )
                arquivo.write(linha)
        print("\nArquivo salvo com sucesso!")

    except OSError as erro:
        print("\nErro ao salvar o arquivo.")
        print("Detalhes:", erro)


def carregar():

    try:
        with open("livros.txt", "r") as arquivo:
            livros.clear()
            for linha in arquivo:
                dados = linha.strip().split(";")
                titulo = dados[0]
                autor = dados[1]
                ano = int(dados[2])
                editora = dados[3]
                preco = float(dados[4])

                livro = Livro(
                    titulo,
                    autor,
                    ano,
                    editora,
                    preco
                )

                livros.append(livro)

        print("\nArquivo carregado com sucesso!")

    except FileNotFoundError:
        print("\nArquivo livros.txt não encontrado.")

    except ValueError:
        print("\nExiste um valor inválido no arquivo.")

    except IndexError:
        print("\nExistem dados incompletos no arquivo.")

    except OSError as erro:
        print("\nErro ao acessar o arquivo.")
        print("Detalhes:", erro)
