# EXEMPLO 06 - ARMAZENANDO OS DADOS

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

resposta = requests.get(url)

soup = BeautifulSoup(resposta.text, "html.parser")

citacoes = soup.find_all("div", class_="quote")

dados = []

for citacao in citacoes:

    texto = citacao.find("span",class_="text").get_text(strip=True)

    autor = citacao.find("small",class_="author").get_text(strip=True)

    registro = {
        "citacao": texto,
        "autor": autor
    }

    dados.append(registro)

# Mostra os dados coletados
for registro in dados:

    print("Autor:", registro["autor"])
    print("Citação:", registro["citacao"])
    print()