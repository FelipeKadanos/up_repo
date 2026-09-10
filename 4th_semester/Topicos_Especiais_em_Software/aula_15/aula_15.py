# PERSISTENCIA DE DADOS COM SQLITE

# SQLite permite integrar a aplicacao Python com um banco de dados local.
# O modulo sqlite3 faz parte da biblioteca padrao do Python.

import sqlite3


def conectar():
    return sqlite3.connect("faculdade.db")


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            curso TEXT
        )
    """)

    conexao.commit()
    conexao.close()


def cadastrar(nome, idade, curso):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO alunos (nome, idade, curso)
        VALUES (?, ?, ?)
    """, (nome, idade, curso))

    conexao.commit()
    conexao.close()


def listar():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")
    dados = cursor.fetchall()
    conexao.close()

    return dados


def procurar(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM alunos
        WHERE nome = ?
    """, (nome,))

    aluno = cursor.fetchone()
    conexao.close()

    return aluno


def alterar_curso(nome, novo_curso):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE alunos
        SET curso = ?
        WHERE nome = ?
    """, (novo_curso, nome))

    conexao.commit()
    conexao.close()


def excluir(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM alunos
        WHERE nome = ?
    """, (nome,))

    conexao.commit()
    conexao.close()


criar_tabela()
cadastrar("Ana", 20, "Engenharia")
cadastrar("Carlos", 22, "Computacao")

print(listar())
print(procurar("Ana"))

alterar_curso("Ana", "Sistemas De Informacao")
print(procurar("Ana"))

excluir("Carlos")
print(listar())
