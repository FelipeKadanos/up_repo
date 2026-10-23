import requests
from bs4 import BeautifulSoup
from flask import request
#EXEMPLO 01 - verificar se conseguimos acessar
url = "https://quotes.toscrape.com/"

resposta = requests.get(url)

print("Status:",resposta.status_code)
# 200 → página acessada com sucesso
# 404 → página não encontrada
# 403 → acesso recusado
# 500 → erro no servidor

#EXEMPLO 02 - RECEBER E INTERPRETAR O HTML
# Interpreta o HTML recebido
soup = BeautifulSoup(resposta.text, "html.parser")

# Exibe o HTML de forma organizada
print(soup.prettify())

# EXEMPLO 03 - LOCALIZAR AS CITAÇÕES

#Localiza todos os blocos de citações
citacoes = soup.find_all("div", class_="quote")
print("Quantidade encontrada:", len(citacoes))

# EXEMPLO 04 - EXTRAIR CITAÇÃO E AUTOR

for citacao in citacoes:
    # Procura o texto dentro do bloco atual
    texto = citacao.find("span", class_="text")
    # Procura o autor dentro do mesmo bloco
    autor = citacao.find("small", class_="author")

    print("Citação:", texto.get_text(strip=True))
    print("Autor:", autor.get_text(strip=True))
    print("---------------------------------------")

# EXEMPLO 05 - COLETANDO TAMBÉM AS TAGS
    # Uma citação pode possuir várias tags

    tags = citacao.find_all("a", class_="tag")

    print("Tags:")
    for tag in tags:
        print("-", tag.get_text(strip=True))
    print("----------------------------------------")




