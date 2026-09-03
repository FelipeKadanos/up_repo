def menu():

    print("\n============================")
    print("     CADASTRO DE LIVROS")
    print("============================")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Procurar livro")
    print("4 - Alterar livro")
    print("5 - Excluir livro")
    print("6 - Salvar arquivo")
    print("7 - Carregar arquivo")
    print("8 - Exibir estatísticas")
    print("0 - Sair")
    print("============================")

    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        print("\nDigite apenas números.")
        return -1
    
