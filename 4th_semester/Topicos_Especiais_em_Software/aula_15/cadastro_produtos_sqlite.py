# EXERCICIO - CADASTRO DE PRODUTOS COM SQLITE

import sqlite3


BANCO = "produtos.db"


def conectar():
    try:
        return sqlite3.connect(BANCO)
    except sqlite3.Error as erro:
        print("Erro ao conectar no banco:", erro)
        return None


def criar_tabela():
    conexao = conectar()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT,
                preco REAL,
                quantidade INTEGER
            )
        """)
        conexao.commit()
    except sqlite3.Error as erro:
        print("Erro ao criar tabela:", erro)
    finally:
        conexao.close()


def cadastrar_produto():
    nome = input("Nome: ").strip().title()
    categoria = input("Categoria: ").strip().title()
    preco = float(input("Preco: "))
    quantidade = int(input("Quantidade: "))

    conexao = conectar()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO produto (nome, categoria, preco, quantidade)
            VALUES (?, ?, ?, ?)
        """, (nome, categoria, preco, quantidade))
        conexao.commit()
        print("Produto cadastrado com sucesso!")
    except sqlite3.Error as erro:
        print("Erro ao cadastrar produto:", erro)
    finally:
        conexao.close()


def listar_produtos():
    conexao = conectar()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produto")
        produtos = cursor.fetchall()

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
            return

        for id_produto, nome, categoria, preco, quantidade in produtos:
            print("----------------------")
            print("Codigo:", id_produto)
            print("Nome:", nome)
            print("Categoria:", categoria)
            print("Preco:", preco)
            print("Quantidade:", quantidade)
    except sqlite3.Error as erro:
        print("Erro ao listar produtos:", erro)
    finally:
        conexao.close()


def procurar_produto():
    nome = input("Nome do produto: ").strip().title()

    conexao = conectar()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT * FROM produto
            WHERE nome = ?
        """, (nome,))
        produto = cursor.fetchone()

        if produto is None:
            print("Produto nao encontrado.")
        else:
            print(produto)
    except sqlite3.Error as erro:
        print("Erro ao procurar produto:", erro)
    finally:
        conexao.close()


def alterar_produto():
    nome = input("Nome do produto que deseja alterar: ").strip().title()
    novo_preco = float(input("Novo preco: "))
    nova_quantidade = int(input("Nova quantidade: "))

    conexao = conectar()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE produto
            SET preco = ?, quantidade = ?
            WHERE nome = ?
        """, (novo_preco, nova_quantidade, nome))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Produto nao encontrado.")
        else:
            print("Produto alterado com sucesso!")
    except sqlite3.Error as erro:
        print("Erro ao alterar produto:", erro)
    finally:
        conexao.close()


def excluir_produto():
    nome = input("Nome do produto que deseja excluir: ").strip().title()

    conexao = conectar()
    if conexao is None:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute("""
            DELETE FROM produto
            WHERE nome = ?
        """, (nome,))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Produto nao encontrado.")
        else:
            print("Produto excluido com sucesso!")
    except sqlite3.Error as erro:
        print("Erro ao excluir produto:", erro)
    finally:
        conexao.close()


def menu():
    while True:
        print("\n1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Procurar produto")
        print("4 - Alterar produto")
        print("5 - Excluir produto")
        print("0 - Sair")

        opcao = input("Opcao: ").strip()

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            procurar_produto()
        elif opcao == "4":
            alterar_produto()
        elif opcao == "5":
            excluir_produto()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opcao invalida.")


criar_tabela()
menu()
