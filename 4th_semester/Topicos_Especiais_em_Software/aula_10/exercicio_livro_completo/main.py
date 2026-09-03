import menu
import cadastro
import arquivo

while True:
    opcao = menu.menu()
    match opcao:
        case 1:
            cadastro.cadastrar()

        case 2:
            cadastro.listar()

        case 3:
            cadastro.procurar()

        case 4:
            cadastro.alterar()

        case 5:
            cadastro.excluir()

        case 6:
            arquivo.salvar()

        case 7:
            arquivo.carregar()

        case 8:
            cadastro.estatisticas()

        case 0:
            print("\nPrograma encerrado.")
            break

        case _:
            print("\nOpção inválida.")
