# Importa os recursos do Flask
from flask import Flask, render_template, request

# Biblioteca utilizada para acessar páginas da Web
import requests

# Biblioteca utilizada para interpretar o HTML
from bs4 import BeautifulSoup


# Cria a aplicação Flask
app = Flask(__name__)


# ==========================================================
# PÁGINA INICIAL
# ==========================================================

@app.route("/")
def inicio():

    # Mostra a página que contém o formulário
    return render_template("index.html")


# ==========================================================
# ROTA RESPONSÁVEL PELA PESQUISA
# ==========================================================

@app.route("/pesquisar", methods=["POST"])
def pesquisar():

    # Recebe a tag escolhida no formulário
    tag = request.form.get("tag")

    # Monta o endereço que será acessado.
    #
    # Exemplo:
    # https://quotes.toscrape.com/tag/love/
    url = f"https://quotes.toscrape.com/tag/{tag}/"

    # Realiza a requisição para o site
    resposta = requests.get(url)

    # Lista que armazenará as citações
    dados = []

    # Verifica se conseguimos acessar a página
    if resposta.status_code == 200:

        # Interpreta o HTML recebido
        soup = BeautifulSoup(
            resposta.text,
            "html.parser"
        )

        # Procura todos os blocos de citações
        citacoes = soup.find_all(
            "div",
            class_="quote"
        )

        # Percorre todas as citações encontradas
        for citacao in citacoes:

            # Localiza o texto da citação
            texto = citacao.find(
                "span",
                class_="text"
            )

            # Localiza o autor
            autor = citacao.find(
                "small",
                class_="author"
            )

            # Extrai somente o conteúdo textual
            texto = texto.get_text(strip=True)
            autor = autor.get_text(strip=True)

            # Cria um dicionário
            registro = {
                "texto": texto,
                "autor": autor
            }

            # Adiciona o registro na lista
            dados.append(registro)

    # Envia os resultados para o HTML
    return render_template(
        "resultado.html",
        tag=tag,
        citacoes=dados
    )


# ==========================================================
# EXECUÇÃO
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)