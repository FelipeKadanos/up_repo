# AULA 16
import pandas as pd

# Mostra em formato de array
notas = pd.Series([7.5, 8.0, 6.5, 9.0])
print(notas)

dados = {
    "Nome": ["Ana","Carlos","Pedro"],
    "Idade": [20,22,19],
    "Nota": [8.5,7.0,9.0]
}

# Mostra em formato de excel
alunos = pd.DataFrame(dados)
print(alunos)
print(alunos["Nome"])

# Mostra o que eu selecionei
selecionados = alunos[["Nome","Nota"]]
print(selecionados)

alunos = pd.DataFrame(dados)
print(alunos.shape) # retorna o tamanho das colunas e linhas
print(alunos.columns) # retorna o nome das colunas
print(alunos.dtypes) # retorna o tipo das colunas
print(alunos.head(5)) # retorna os 5 primeiros registros
print(alunos.tail(5)) # retorna os 5 ultimos registros
alunos.info # retorna infos sobre o DataFrame

# AULA 16

# SEM PANDAS:
# import csv
# with open("alunos.csv","w",newline="") as arquivo:
    # escritor = csv.writer(arquivo)
    # escritor.writerow(["Nome", "Idade", "Curso"])
    # escritor.writerow(["Ana", 20, "Engenharia"])
    # escritor.writerow(["Carlos", 22, "Computação"])
    # escritor.writerow(["João", 26, "Engenharia"])

# COM PANDAS:
import pandas as pd
dados = pd.read_csv("alunos.csv", encoding="latin-1")

print(dados)
print(dados["Idade"].mean())
print(dados["Idade"].max())
print(dados["Idade"].min())
print(dados.describe())

dados.to_csv("resultado.csv", index=False)