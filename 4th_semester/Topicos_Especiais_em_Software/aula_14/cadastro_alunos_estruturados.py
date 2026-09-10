# EXERCICIO - CADASTRO DE ALUNOS COM CSV E JSON

import csv
import json
import os


PASTA_DADOS = "dados"
CAMINHO_CSV = os.path.join(PASTA_DADOS, "alunos_cadastrados.csv")
CAMINHO_JSON = os.path.join(PASTA_DADOS, "alunos_cadastrados.json")


def garantir_pasta_dados():
    if not os.path.exists(PASTA_DADOS):
        os.mkdir(PASTA_DADOS)


def cadastrar_alunos():
    alunos = []

    while True:
        nome = input("Nome do aluno: ").strip().title()
        idade = int(input("Idade: "))
        curso = input("Curso: ").strip().title()

        alunos.append({
            "nome": nome,
            "idade": idade,
            "curso": curso,
        })

        continuar = input("Deseja cadastrar outro aluno? [s/n] ").strip().lower()
        if continuar != "s":
            break

    return alunos


def salvar_csv(alunos):
    with open(CAMINHO_CSV, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["nome", "idade", "curso"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(alunos)


def ler_csv():
    with open(CAMINHO_CSV, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)


def salvar_json(alunos):
    with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, indent=4, ensure_ascii=False)


def ler_json():
    with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def mostrar_alunos(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print("----------------------")
        print("Nome:", aluno["nome"])
        print("Idade:", aluno["idade"])
        print("Curso:", aluno["curso"])


def main():
    garantir_pasta_dados()
    alunos = cadastrar_alunos()

    salvar_csv(alunos)
    print("\nDados lidos do CSV:")
    mostrar_alunos(ler_csv())

    salvar_json(alunos)
    print("\nDados lidos do JSON:")
    mostrar_alunos(ler_json())


if __name__ == "__main__":
    main()
