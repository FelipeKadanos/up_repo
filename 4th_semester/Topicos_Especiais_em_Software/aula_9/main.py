from menu import menu
from cadastro import cadastrar
from cadastro import listar
from cadastro import pesquisar
from arquivo import salvar
from arquivo import carregar

while True:
    
    opcao = menu()
    match opcao:
        case 1:
            cadastrar()
        case 2:
            listar()
        case 3:
            pesquisar()
        case 4:
            salvar()
        case 5:
            carregar()
        case 0:
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")