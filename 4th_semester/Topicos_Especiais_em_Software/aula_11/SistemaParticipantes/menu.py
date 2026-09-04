def menu():

    print("\n==================================")
    print(" GERENCIAMENTO DE PARTICIPANTES")
    print("==================================")
    print("1 - Cadastrar participante")
    print("2 - Listar participantes")
    print("3 - Pesquisar participante")
    print("4 - Alterar participante")
    print("5 - Excluir participante")
    print("6 - Exibir estatísticas")
    print("7 - Salvar arquivo")
    print("8 - Carregar arquivo")
    print("0 - Sair")
    print("==================================")

    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        print("\nDigite apenas números.")
        return -1