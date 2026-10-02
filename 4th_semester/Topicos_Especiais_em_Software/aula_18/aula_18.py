# AULA 18
# Felipe e Marcos

# 1: (FEITO)
# a) Identificar qtd registros
# a) Verificar dados ausentes
# a) Realizar tratamento adequado quando necessario

import pandas as pd
import numpy as np
dados = pd.read_csv("Atividade2.csv")
qtdRegistros = len(dados)
colunas = len(dados.loc[0])

print(qtdRegistros)
print(colunas)

condicao = (dados["bmi"] == "N/A") | (dados["smoking_status"] == "Unknown")
nulos = condicao.sum()
print("Quantidade de registros nulos:", nulos)



# 1. Converter "N/A" do bmi para NaN (formato padrão de dado ausente no Pandas)
dados["bmi"] = dados["bmi"].replace("N/A", np.nan)
dados["bmi"] = pd.to_numeric(dados["bmi"])

# 2. Tratamento do BMI: Preencher os vazios com a mediana da coluna
mediana_bmi = dados["bmi"].median()
dados["bmi"] = dados["bmi"].fillna(mediana_bmi)

# 3. Tratamento do Smoking Status: Onde for "Unknown", substituir por um valor padrão (ex: "Other" ou NaN)
dados.loc[dados["smoking_status"] == "Unknown", "smoking_status"] = "Not informed"
print("Dados tratados com sucesso!")



condicao = (dados["bmi"] == "N/A") | (dados["smoking_status"] == "Unknown")
nulos = condicao.sum()
print("Quantidade de registros nulos depois do tratamento:", nulos)

