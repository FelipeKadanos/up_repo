from dados import participantes
from participante import Participante


def salvar():
    try:
        with open("participantes.txt", "w") as arquivo:
            for participante in participantes:
                linha = (
                    participante.nome + ";" +
                    str(participante.idade) + ";" +
                    participante.email + ";" +
                    participante.categoria + ";" +
                    str(participante.valor_pago) + "\n"
                )
                arquivo.write(linha)
        print("\nArquivo salvo com sucesso!")

    except OSError as erro:
        print("\nErro ao salvar o arquivo.")
        print("Detalhes:", erro)


def carregar():
    try:
        with open("participantes.txt", "r") as arquivo:
            participantes.clear()
            for linha in arquivo:
                dados = linha.strip().split(";")
                nome = dados[0]
                idade = int(dados[1])
                email = dados[2]
                categoria = dados[3]
                valor_pago = float(dados[4])

                participante = Participante(
                    nome,
                    idade,
                    email,
                    categoria,
                    valor_pago
                )

                participantes.append(participante)

        print("\nArquivo carregado com sucesso!")

    except FileNotFoundError:
        print("\nArquivo participantes.txt não encontrado.")

    except ValueError:
        print("\nExiste um valor inválido no arquivo.")

    except IndexError:
        print("\nExistem dados incompletos no arquivo.")

    except OSError as erro:
        print("\nErro ao acessar o arquivo.")
        print("Detalhes:", erro)
