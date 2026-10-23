# Importa a biblioteca responsável por acessar páginas da Web
import requests

# Importa o BeautifulSoup, utilizado para interpretar o HTML
from bs4 import BeautifulSoup

# Importa o Pandas para organizar e salvar os dados
import pandas as pd


# Lista que armazenará todas as citações coletadas
dados = []


# ============================================================
# COLETA DOS DADOS
# ============================================================

# O site possui várias páginas.
# Neste exemplo, vamos acessar as três primeiras páginas.
for pagina in range(1, 4):

    # Monta o endereço da página que será acessada.
    # Quando pagina = 1:
    # https://quotes.toscrape.com/page/1/
    #
    # Quando pagina = 2:
    # https://quotes.toscrape.com/page/2/
    url = f"https://quotes.toscrape.com/page/{pagina}/"

    print(f"\nAcessando página {pagina}...")

    # Realiza a requisição para o site
    resposta = requests.get(url)

    # Verifica se a página foi acessada corretamente
    if resposta.status_code == 200:

        print("Página acessada com sucesso!")

        # Converte o HTML recebido em uma estrutura
        # que o BeautifulSoup consegue pesquisar
        soup = BeautifulSoup(resposta.text,"html.parser")

        # Localiza todos os blocos que representam
        # uma citação na página
        citacoes = soup.find_all("div",class_="quote")

        # Percorre todas as citações encontradas
        for citacao in citacoes:

            # ------------------------------------------------
            # TEXTO DA CITAÇÃO
            # ------------------------------------------------

            # Procura:
            # <span class="text">
            texto = citacao.find("span",class_="text")

            # Extrai somente o conteúdo textual
            texto = texto.get_text(strip=True)


            # ------------------------------------------------
            # AUTOR
            # ------------------------------------------------

            # Procura:
            # <small class="author">
            autor = citacao.find("small",class_="author")

            # Extrai somente o nome do autor
            autor = autor.get_text(strip=True)


            # ------------------------------------------------
            # TAGS
            # ------------------------------------------------

            # Uma citação pode possuir várias tags.
            #
            # Por isso utilizamos find_all().
            tags_html = citacao.find_all("a",class_="tag")

            # Lista para armazenar as tags
            lista_tags = []

            # Percorre as tags encontradas
            for tag in tags_html:

                # Extrai somente o texto da tag
                nome_tag = tag.get_text(strip=True)

                # Adiciona a tag na lista
                lista_tags.append(nome_tag)


            # ------------------------------------------------
            # ORGANIZAÇÃO DOS DADOS
            # ------------------------------------------------

            # Cada citação será representada
            # por um dicionário.
            registro = {
                "citacao": texto,
                "autor": autor,
                "tags": ", ".join(lista_tags) #Pegue todas as tags da lista e transforme em uma
                                              # única string, separando cada uma por vírgula e espaço.
            }

            # Adiciona o dicionário à lista principal
            dados.append(registro)

    else:

        # Será executado se não conseguirmos
        # acessar determinada página
        print("Erro ao acessar a página.","Código:",resposta.status_code)


# ============================================================
# APRESENTAÇÃO DOS RESULTADOS
# ============================================================

print("\n")
print("=" * 60)
print("RESULTADO DA COLETA")
print("=" * 60)


# Percorre todos os registros armazenados
for registro in dados:

    print("\nAutor:")
    print(registro["autor"])

    print("\nCitação:")
    print(registro["citacao"])

    print("\nTags:")
    print(registro["tags"])

    print("-" * 60)


# ============================================================
# TOTAL DE REGISTROS
# ============================================================

print("\nTotal de citações coletadas:", len(dados))


# ============================================================
# CRIAÇÃO DO DATAFRAME
# ============================================================

# Transforma a lista de dicionários
# em um DataFrame do Pandas
df = pd.DataFrame(dados)


# Mostra o DataFrame
print("\nDados organizados:")
print(df)


# ============================================================
# SALVANDO EM CSV
# ============================================================

# Salva os dados coletados em um arquivo CSV
df.to_csv("citacoes.csv",index=False,encoding="utf-8")

print("\nArquivo citacoes.csv criado com sucesso!")