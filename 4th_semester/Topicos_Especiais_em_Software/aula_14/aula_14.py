# ARQUIVOS ESTRUTURADOS

# Em TXT, nos mesmos definimos como separar os campos.
# CSV, JSON e XML possuem estruturas proprias para representar dados.

import csv
import json
import os
import xml.etree.ElementTree as ET


# MANIPULACAO DE DIRETORIOS
print(os.getcwd())

for arquivo in os.listdir():
    print(arquivo)

if not os.path.exists("dados"):
    os.mkdir("dados")


# CSV - GRAVANDO
alunos = [
    ["Ana", 20, "Engenharia"],
    ["Carlos", 22, "Computacao"],
    ["Pedro", 19, "Administracao"],
]

with open("dados/alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Idade", "Curso"])
    escritor.writerows(alunos)


# CSV - LENDO
with open("dados/alunos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)


# CSV COM DICIONARIOS
with open("dados/alunos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for aluno in leitor:
        print(aluno["Nome"])
        print(aluno["Idade"])
        print(aluno["Curso"])


# JSON - GRAVANDO
aluno = {
    "nome": "Ana",
    "idade": 20,
    "curso": "Engenharia",
}

with open("dados/aluno.json", "w", encoding="utf-8") as arquivo:
    json.dump(aluno, arquivo, indent=4, ensure_ascii=False)


# JSON - LENDO
with open("dados/aluno.json", "r", encoding="utf-8") as arquivo:
    aluno = json.load(arquivo)

print(aluno["nome"])
print(aluno["idade"])
print(aluno["curso"])


# XML - LENDO
xml = """<aluno>
    <nome>Ana</nome>
    <idade>20</idade>
    <curso>Engenharia</curso>
</aluno>"""

with open("dados/aluno.xml", "w", encoding="utf-8") as arquivo:
    arquivo.write(xml)

arvore = ET.parse("dados/aluno.xml")
raiz = arvore.getroot()

print(raiz.find("nome").text)
print(raiz.find("idade").text)
print(raiz.find("curso").text)
