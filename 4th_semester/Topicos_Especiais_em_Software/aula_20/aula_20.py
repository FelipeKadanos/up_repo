import requests
from bs4 import BeautifulSoup


# EXEMPLO 1 - VERIFICAR CONEXÃO
url = "http://quotes.toscrape.com/"
print(url)
resposta = requests.get(url)
print(resposta.status_code)  # 200 = OK, 404 = NOT FOUND, 500 = INTERNAL SERVER ERROR


# EXEMPLO 2 - RECEBER E INTEPRETAR O HTML
soup = BeautifulSoup(resposta.text, "html.parser")
# print(soup.prettify())  # imprime o HTML de forma organizada


# EXEMPLO 3 - LOCALIZAR CITAÇÕES
citacoes = soup.find_all("div", class_="quote")
print("Quantiaddde e]ncontrada: ", len(citacoes))


# EXEMPLO 4 - IMPRIMIR CITAÇÕES
for citacao in citacoes:
    texto = citacao.find("span", class_="text")
    autor = citacao.find("small", class_="author")
    print("Citação: ", texto.get_text(strip=True))
    print("Autor: ", autor.get_text(strip=True))


# EXEMPLO 5 - COLETANDO AS TAGS
    tags = soup.find_all("a", class_="tag")
    print("TAGS: ")
    for tag in tags:
        # print("-", tag.get_text(strip=True))
        
    print("-" * 50) 