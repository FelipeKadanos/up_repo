# AULA 18 - TRABALHO 2
# Felipe e Marcos

import os
import sqlite3

import matplotlib
# Utiliza um modo do Matplotlib que salva os graficos sem precisar abrir uma janela.
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


# Monta os caminhos a partir da pasta do proprio script. Assim, o programa
# encontra o CSV mesmo quando for executado a partir de outra pasta.
PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_CSV = os.path.join(PASTA, "Atividade2.csv")
BANCO = os.path.join(PASTA, "atividade2.db")


def preparar_dados():
    # Le o arquivo CSV e transforma os registros em um DataFrame do Pandas.
    dados = pd.read_csv(ARQUIVO_CSV)

    # Mostra informações antes de realizar qualquer alteracao.
    print("=== PREPARACAO DOS DADOS ===")
    print("Quantidade de registros:", len(dados))
    print("Quantidade de colunas:", len(dados.columns))
    print("Colunas:", list(dados.columns))
    print("\nDados ausentes antes do tratamento:")
    print(dados.isnull().sum())
    print("Smoking status desconhecido:", (dados["smoking_status"] == "Unknown").sum())

    # Alguns pacientes nao possuem BMI. Em vez de remover esses pacientes,
    # calculamos a mediana dos valores existentes e usamos esse valor nos vazios.
    # A mediana foi escolhida por que sofre menos influencia de valores muito altos ou muito baixos.
    mediana_bmi = dados["bmi"].median()
    dados["bmi"] = dados["bmi"].fillna(mediana_bmi)

    # "Unknown" nao e um dado ausente para o Pandas, pois e um texto. Trocamos
    # por "Not informed" para deixar claro que o paciente nao informou o dado.
    dados.loc[dados["smoking_status"] == "Unknown", "smoking_status"] = "Not informed"

    # Faz uma nova verificacao para comprovar que o tratamento foi realizado.
    print("\nMediana usada para preencher o BMI:", mediana_bmi)
    print("Dados ausentes depois do tratamento:", dados.isnull().sum().sum())
    print("Smoking status desconhecido depois do tratamento:",
          (dados["smoking_status"] == "Unknown").sum())

    return dados


def analisar_dados(dados):
    # Filtra o DataFrame e cria um grupo com AVC e outro sem AVC.
    # No dataset, stroke igual a 1 significa com AVC e 0 significa sem AVC.
    com_avc = dados[dados["stroke"] == 1]
    sem_avc = dados[dados["stroke"] == 0]

    print("\n=== ANALISE DOS DADOS ===")
    print("Pacientes com AVC:", len(com_avc))
    print("Pacientes sem AVC:", len(sem_avc))

    # Agrupa os pacientes pela coluna stroke e calcula a media das caracteristicas.
    # Nas colunas hypertension e heart_disease, 1 significa sim e 0 significa nao.
    # Por isso, a media dessas colunas representa a proporcao de pacientes com a condicao.
    colunas = ["age", "hypertension", "heart_disease", "avg_glucose_level", "bmi"]
    comparacao = dados.groupby("stroke")[colunas].mean().round(2)
    print("\nMedias por grupo (0 = sem AVC e 1 = com AVC):")
    print(comparacao)

    # Cria uma tabela cruzada para contar cada situacao de tabagismo nos dois grupos.
    tabagismo = pd.crosstab(dados["smoking_status"], dados["stroke"])
    print("\nSituacao de tabagismo por grupo:")
    print(tabagismo)

    print("\nInterpretacao:")
    print("Os pacientes com AVC possuem maior idade media, maior glicose media e maior BMI medio.")
    print("Hipertensao e doenca cardiaca tambem sao mais frequentes no grupo com AVC.")
    print("Essas diferencas foram observadas neste dataset e nao comprovam causa do AVC.")


def criar_graficos(dados):
    # O primeiro grafico utiliza somente as idades dos pacientes com AVC.
    com_avc = dados[dados["stroke"] == 1]

    # O histograma divide as idades em 10 intervalos e conta quantos pacientes
    # estao em cada intervalo.
    plt.hist(com_avc["age"], bins=10, color="steelblue", edgecolor="black")
    plt.title("Distribuicao das idades dos pacientes com AVC")
    plt.xlabel("Idade")
    plt.ylabel("Quantidade de pacientes")
    plt.tight_layout()
    plt.savefig(os.path.join(PASTA, "grafico_1_idades_avc.png"))
    plt.close()

    # Calcula a glicose media de cada grupo para fazer uma comparacao em barras.
    glicose_media = dados.groupby("stroke")["avg_glucose_level"].mean()
    glicose_media.index = ["Sem AVC", "Com AVC"]
    glicose_media.plot(kind="bar", color=["green", "red"])
    plt.title("Nivel medio de glicose por grupo")
    plt.xlabel("Grupo")
    plt.ylabel("Nivel medio de glicose")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(PASTA, "grafico_2_glicose.png"))
    plt.close()

    # Como hypertension possui apenas 0 e 1, sua media e a proporcao de pessoas
    # com hipertensao. Multiplicamos por 100 para transformar em percentual.
    hipertensao = dados.groupby("stroke")["hypertension"].mean() * 100
    hipertensao.index = ["Sem AVC", "Com AVC"]
    hipertensao.plot(kind="bar", color=["green", "red"])
    plt.title("Percentual de pacientes com hipertensao")
    plt.xlabel("Grupo")
    plt.ylabel("Pacientes com hipertensao (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(PASTA, "grafico_3_hipertensao.png"))
    plt.close()

    print("\nTres graficos foram salvos na pasta do trabalho.")


def salvar_banco(dados):
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()

    # Apaga a tabela anterior para nao duplicar os registros ao executar novamente.
    cursor.execute("DROP TABLE IF EXISTS pacientes")

    # Cria uma coluna no banco para cada coluna existente no arquivo CSV.
    cursor.execute("""
        CREATE TABLE pacientes (
            id INTEGER PRIMARY KEY,
            gender TEXT,
            age REAL,
            hypertension INTEGER,
            heart_disease INTEGER,
            ever_married TEXT,
            work_type TEXT,
            residence_type TEXT,
            avg_glucose_level REAL,
            bmi REAL,
            smoking_status TEXT,
            stroke INTEGER
        )
    """)

    # Converte cada linha do DataFrame em uma tupla. O executemany insere todas
    # essas tuplas no banco usando uma unica instrucao SQL.
    registros = list(dados.itertuples(index=False, name=None))
    cursor.executemany("""
        INSERT INTO pacientes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, registros)
    conexao.commit()

    print("\n=== CONSULTAS AO BANCO ===")

    # Consulta 1: conta todos os registros salvos na tabela.
    cursor.execute("SELECT COUNT(*) FROM pacientes")
    print("1. Total de registros armazenados:", cursor.fetchone()[0])

    # Consulta 2: seleciona os pacientes com AVC. Somente os cinco primeiros
    # sao mostrados para evitar a impressao de 249 linhas no terminal.
    cursor.execute("SELECT * FROM pacientes WHERE stroke = 1")
    pacientes_com_avc = cursor.fetchall()
    print("2. Quantidade de pacientes com AVC:", len(pacientes_com_avc))
    print("Primeiros 5 pacientes com AVC:")
    for paciente in pacientes_com_avc[:5]:
        print(paciente)

    # Consulta 3: calcula a idade media somente dos pacientes com hipertensao.
    cursor.execute("""
        SELECT ROUND(AVG(age), 2)
        FROM pacientes
        WHERE hypertension = 1
    """)
    print("3. Idade media dos pacientes com hipertensao:", cursor.fetchone()[0])

    conexao.close()
    print("Banco de dados salvo em atividade2.db.")


def main():
    dados = preparar_dados()
    analisar_dados(dados)
    criar_graficos(dados)
    salvar_banco(dados)


if __name__ == "__main__":
    main()
