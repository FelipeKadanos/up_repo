# AULA 18 - TRABALHO 2
# Felipe Kadanos e Marcos Ferrari


import os
import sqlite3

import matplotlib
matplotlib.use("Agg") # Utiliza um modo do Matplotlib que salva os graficos sem precisar abrir uma janela.
import matplotlib.pyplot as plt
import pandas as pd



# __file__ : Caminho do arquivo atual (trab_2.py)
# os.path.abspath(...): Transforma o caminho em um caminho absoluto, completo
# os.path.dirname(...): Pega somente a parte correspondente à pasta
# os.path.join(): Junta a pasta com o nome do arquivo
PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_CSV = os.path.join(PASTA, "Atividade2.csv")
BANCO = os.path.join(PASTA, "atividade2.db")



# Preenche os dados ausentes e imprime informacoes sobre o dataset.
def preparar_dados():
    dados = pd.read_csv(ARQUIVO_CSV)

    print("=== PREPARACAO DOS DADOS ===")
    print("Quantidade de registros:", len(dados))
    print("Quantidade de colunas:", len(dados.columns))
    print("Colunas:", list(dados.columns))
    print("\n\nDados ausentes antes do tratamento:")
    print(dados.isnull().sum())
    
    # Decisão: Como tratar o tabagismo não informado?
    # Mantemos Unknown porque não sabemos se esses pacientes fumam.
    # Assim, eles continuam na análise sem inventarmos uma informação.
    desconhecidos = (dados["smoking_status"] == "Unknown").sum()
    print("Tabagismo nao informado (Unknown):", desconhecidos)

    # Decisão: Como preencher os valores ausentes de BMI?
    # Usamos a mediana porque ela sofre menos influência de valores muito altos ou baixos.
    # Preencher os valores permite manter todos os pacientes na análise.
    mediana_bmi = dados["bmi"].median() # Não confundir com a função da media: mean()
    
    # Preenche o BMI dos pacientes que não informaram
    dados["bmi"] = dados["bmi"].fillna(mediana_bmi)

    print("\n\nMediana usada para preencher o BMI:", mediana_bmi)
    # isnull() marca os valores nulos. O primeiro sum() conta por coluna e o segundo soma o total.
    print("Valores nulos depois do tratamento:", dados.isnull().sum().sum()) # isnull() retorno true ou false, sum() transforma em 1 ou 0, sum() soma tudo, ou seja, retorna a quantidade de valores nulos. 
    print("Os casos Unknown permanecem identificados como tabagismo nao informado.")

    return dados



def analisar_dados(dados):
    # Filtra o DataFrame e cria um grupo com AVC e outro sem AVC.
    com_avc = dados[dados["stroke"] == 1] # stroke == 1 significa com AVC
    sem_avc = dados[dados["stroke"] == 0] # stroke == 0 significa sem AVC

    print("\n\n\n=== ANALISE DOS DADOS ===")
    print("Pacientes com AVC:", len(com_avc))
    print("Pacientes sem AVC:", len(sem_avc))

    # Decisão: Como comparar idade, glicose e BMI entre os grupos?
    # Usamos a média de cada grupo para resumir os valores e comparar as diferenças.
    colunas = ["age", "hypertension", "heart_disease", "avg_glucose_level", "bmi"]
    medias = dados.groupby("stroke")[colunas].mean() # Faz a media das colunas, agrupadas por stroke

    # Decisão: Como comparar hipertensão e doença cardíaca entre os grupos?
    # Usamos percentuais porque os grupos têm quantidades diferentes de pacientes.
    # Como essas colunas têm só 0 e 1, a média já representa a proporção com a condição.
    comparacao = medias.copy()
    # Media ja foi feita no mean(), então so multiplicamos por 100 para transformar em percentual
    comparacao["hypertension"] = comparacao["hypertension"] * 100
    comparacao["heart_disease"] = comparacao["heart_disease"] * 100

    print("\n\nComparacao por grupo (0 = sem AVC e 1 = com AVC):")
    print("Hipertensao e doenca cardiaca em %; demais colunas em medias.")
    print(comparacao.round(2).to_string())

    # Decisão: Como comparar as situações de tabagismo?
    # Contamos os pacientes de cada categoria e calculamos o percentual dentro de cada grupo.
    # Isso permite comparar os grupos mesmo com quantidades diferentes de pacientes.
    # pd.crosstab() permite comparar as colunas, mostrando a quantidade de pacientes em cada categoria
    tabagismo = pd.crosstab(dados["smoking_status"], dados["stroke"])
    print("\n\nSituacao de tabagismo por grupo:")
    print(tabagismo)

    # Compara os grupos proporcionalmente, mostrando a porcentagem de cada categoria em relacao ao total de pacientes com e sem AVC.
    percentuais_tabagismo = tabagismo / tabagismo.sum() * 100
    print("\n\nTabagismo em % de cada grupo:")
    print(percentuais_tabagismo.round(2))

    print("\n\nInterpretacao:")
    print("Os pacientes com AVC possuem maior idade media, maior glicose media e maior BMI medio.")
    print("Hipertensao e doenca cardiaca tambem sao mais frequentes no grupo com AVC.")
    print("A proporcao de ex-fumantes e maior no grupo com AVC.")
    print("Essas diferencas foram observadas neste dataset e nao comprovam causa do AVC.")

    return medias



def criar_graficos(dados, medias):
    # 1- Mostra a distribuicao das idades dos pacientes com AVC 
    # Utiliza somente as **idades** dos pacientes **com AVC**
    com_avc = dados[dados["stroke"] == 1]

    # Decisão: Como mostrar a distribuição das idades no primeiro gráfico?
    # Usamos um histograma para mostrar em quais faixas de idade há mais pacientes com AVC.
    # Escolhemos 10 intervalos para agrupar as idades e facilitar a leitura.
    # O histograma divide as idades em 10 intervalos e conta quantos pacientes estao em cada intervalo.
    plt.hist(com_avc["age"], bins=10, color="steelblue", edgecolor="black")
    plt.title("Distribuicao das idades dos pacientes com AVC")   # Titulo
    plt.xlabel("Idade")                                          # Legenda do eixo X
    plt.ylabel("Quantidade de pacientes")                        # Legenda do eixo Y
    plt.tight_layout()                                           # Evita sobreposicao de elementos
    plt.savefig(os.path.join(PASTA, "grafico_1_idades_avc.png")) # Salva o grafico em um arquivo
    plt.close()

    # 2- Mostra a media de glicose dos pacientes com e sem AVC 
    # Decisão: Qual característica comparar no segundo gráfico?
    # Escolhemos a glicose porque sua média é maior no grupo com AVC neste conjunto de dados.
    # Usamos barras para facilitar a comparação das duas médias.
    # Utiliza a media de glicose dos pacientes com e sem AVC
    glicose_media = medias["avg_glucose_level"].copy()
    glicose_media.index = ["Sem AVC", "Com AVC"]
    glicose_media.plot(kind="bar", color=["green", "red"])

    plt.title("Nivel medio de glicose por grupo")             # Titulo
    plt.xlabel("Grupo")                                       # Legenda do eixo X
    plt.ylabel("Nivel medio de glicose")                      # Legenda do eixo Y
    plt.xticks(rotation=0)                                    # Deixa os textos do eixo X na horizontal
    plt.tight_layout()                                        # Evita sobreposicao de elementos
    plt.savefig(os.path.join(PASTA, "grafico_2_glicose.png")) # Salva o grafico em um arquivo
    plt.close()
    
    # 3- Mostra a proporcao de pacientes com hipertensao nos grupos com e sem AVC 
    # Decisão: Qual informação escolher para o terceiro gráfico e por quê?
    # Escolhemos a hipertensão porque ela aparece em 26,51% do grupo com AVC e 8,89% do grupo sem AVC.
    # As barras ajudam a visualizar essa diferença, que não prova que a hipertensão causou o AVC.
    # Utiliza a media de hipertensao dos pacientes com e sem AVC
    # Hypertension possui so 0 e 1, sua media é a proporcao de pessoas com hipertensao. Multiplicamos por 100 para transformar em percentual.
    hipertensao = medias["hypertension"] * 100
    hipertensao.index = ["Sem AVC", "Com AVC"]
    hipertensao.plot(kind="bar", color=["green", "red"])
    plt.title("Percentual de pacientes com hipertensao")          # Titulo
    plt.xlabel("Grupo")                                           # Legenda do eixo X
    plt.ylabel("Pacientes com hipertensao (%)")                   # Legenda do eixo Y
    plt.xticks(rotation=0)                                        # Deixa os textos do eixo X na horizontal
    plt.tight_layout()                                            # Evita sobreposicao de elementos
    plt.savefig(os.path.join(PASTA, "grafico_3_hipertensao.png")) # Salva o grafico em um arquivo
    plt.close()

    print("\n\nTres graficos foram salvos na pasta do trabalho.")



def salvar_banco(dados):
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()

    # Decisão: Como gravar os dados tratados no SQLite?
    # Usamos to_sql porque os dados já estão em um DataFrame e podemos gravá-los com uma chamada.
    # Isso deixa essa parte do código mais curta e fácil de acompanhar.
    # to_sql (do Pandas) : cria a tabela e grava os dados tratados.
    # replace :  recria a tabela, evitando duplicacao ao executar novamente.
    # index=False : não grava o indice do DataFrame como uma coluna extra.
    dados.to_sql("pacientes", conexao, if_exists="replace", index=False)

    print("\n\n\n=== CONSULTAS AO BANCO ===")

    # Consulta 1: conta todos os registros salvos na tabela.
    cursor.execute("SELECT COUNT(*) FROM pacientes")
    print("1. Total de registros armazenados:", cursor.fetchone()[0])

    # Consulta 2: seleciona os pacientes com AVC. Somente os cinco primeiros
    cursor.execute("SELECT COUNT(*) FROM pacientes WHERE stroke = 1")
    print("2. Quantidade de pacientes com AVC:", cursor.fetchone()[0])

    cursor.execute("SELECT * FROM pacientes WHERE stroke = 1 LIMIT 5")
    print("Primeiros 5 pacientes com AVC:", cursor.fetchall())

    # Consulta 3: calcula a idade media somente dos pacientes com hipertensao.
    # Decisão: Qual consulta livre fazer no banco?
    # Escolhemos a idade média dos hipertensos para conhecer a idade desse grupo.
    # Essa consulta usa duas características analisadas no trabalho: idade e hipertensão.
    cursor.execute("SELECT ROUND(AVG(age), 2) FROM pacientes WHERE hypertension = 1")
    print("3. Idade media dos pacientes com hipertensao:", cursor.fetchone()[0])

    conexao.close()
    print("Banco de dados salvo em atividade2.db.")



def main():
    dados = preparar_dados()
    medias = analisar_dados(dados)
    criar_graficos(dados, medias)
    salvar_banco(dados)



main()
