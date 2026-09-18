# AULA 17

import pandas as pd
dados = pd.read_csv("alunos.csv")
print(dados.loc[0]) # Mostra o nome das colunas ao inves do indice
print(dados.loc[0, "Nome"]) # Valor de Nome
print(dados.loc[0:2]) # Exibe ate a 3° linha
print(dados.loc[0:2, ["Nome", "Nota"]])


print(dados.iloc[0,1]) # 0 = linha; 1 = coluna

# Os dois mostram a mesma coisa, porem de maneiras diferenças
print(dados.loc[0, "Curso"])
print(dados.iloc[0,1])


resultado = (dados["Nota"] >= 7) & (dados["Frequencia"] >= 75)
print(resultado)

resultado1 = (dados["Curso"] == "Computação") | (dados["Nota"] >= 9)
print(resultado1)

print(dados.isnull().sum())

dados_limpos = dados.dropna() # remove os registros nulos

dados["Nota"] = (dados["Nota"].fillna(0)) # preenche os valores null com 0

# Criando uma coluna
dados["Situacao"] = dados["Nota"].apply(lambda Nota: "Aprovado" if Nota >= 7 else "Reprovado")



# UTILIZANDO O OUTRO ARQUIVO
import pandas as pd
dados = pd.read_csv("vendas.csv")

total_regiao = (dados.groupby("Regiao")["Valor"].sum())
print(total_regiao)

media_regiao = (dados.groupby("Regiao")["Valor"].mean())
print(media_regiao)

total_vendedor = (dados.groupby("Vendedor")["Valor"].sum())
print(total_vendedor)

resultado = ((dados.groupby(["Regiao", "Categoria"])["Valor"].sum()))
print(resultado)

resultado = ((dados.groupby("Regiao")["Valor"].agg(["sum", "mean", "min", "max"])))
print(resultado)

# FAZENDO GRAFICOS

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("vendas.csv")

total_regiao = dados.groupby("Regiao")["Valor"].sum()
total_regiao.plot(kind="bar", color=["red", "green"])
plt.title("Total de vendas por região")
plt.xlabel("Região")
plt.ylabel("Valor Total")
plt.xticks(rotation=0) # deixa a leganda na horizontal
plt.tight_layout() # Faz o grafico ficar do tamanho da janela que abrir
plt.savefig("vendas_regiao.png")
plt.show()

total_regiao.plot(kind="pie")
plt.title("Total de vendas por região")
plt.xlabel("Região")
plt.ylabel("Valor Total")
plt.show()