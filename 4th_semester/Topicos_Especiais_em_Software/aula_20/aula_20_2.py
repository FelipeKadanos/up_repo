# EXEMPLO 6 - ARMAZENANDO OS DADOS

import requests 
from bs4 import BeautifulSoup
url = "http://quotes.toscrape.com/"
resposta = requests.get(url)
soup = BeautifulSoup(resposta.text, "html.parser")
citacoes = soup.find_all("div", class_="quote")

dados = []
for citacao in citacoes:
    texto = citacao.find("span", class_="text").get_text(strip=True)
    autor = citacao.find("small", class_="author").get_text(strip=True)

    registro = {
        "citacao": texto,
        "autor": autor
    }

    dados.append(registro)

for registro in dados:
    print("Autor: ", registro["autor"])
    print("Citacao: ", registro["citacao"])
    print()