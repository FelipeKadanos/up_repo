from util import titulo

def menu():
    titulo("CADASTRO DE PRODUTOS")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Pesquisar")
    print("4 - Salvar")
    print("5 - Carregar")
    print("0 - Sair")
    opcao = int(input("\nOpção: "))
    return opcao