def menu():
    print("=" * 30)
    print("SISTEMA DE CADASTRO DE LIVROS")
    print("=" * 30)
    return input("\n1 - Cadastrar \n2 - Listar \n3 - Procurar \n4 - Excluir \n5 - Quantidade \n0 - Sair \nDigite a opção que deseja: ")

def cadastrar():
    livro = {}
    print("Livro ", count + 1)

    livro["nome"] = input(f"Nome do livro:").strip().title()
    livro["autor"] = input(f"Autor:").strip().title()
    livro["ano"] = input(f"Ano:").strip().title()
    livro["editora"] = input(f"Editora:").strip().title()

    arquivo = open("livros.csv","a")
    arquivo.write(";".join(livro))
    arquivo.close()

def listar():
    print("Livros incluidos: ")
    print("Nome | Autor | Ano | Editora ")
            
    with open("livros.csv","r") as arquivo:
        for livro in arquivo:
            print(", ".join(livro))

def procurar():
    procura = input("Digite o livro que deseja: ").strip().title()

    with open("livros.csv","r") as arquivo:
        for livro in arquivo:
            if procura in livro:
                return print(", ".join(livro))

        return print("Não encontrado!")

def excluir():
    exclui = input("Digite o nome do livro que deseja excluir: ").strip().title()
    encontrado = False

    with open("livros.csv","r") as arquivo:
        conteudo = []
        
        for livro in arquivo:
            conteudo.append(livro)
            
            if exclui in livro:
                if conteudo.pop() == True: 
                    return print("Livro removido!") 
                else:
                    return print("Erro ao remover livro.")
        
        return print("Livro não encontrado!")

def contar():
    qtd = 0

    with open("livros.csv","r") as arquivo:
        for livro in arquivo:
            qtd += 1

    print("quantidade de livros: ", qtd)

arquivo = open("livros.csv","w")
arquivo.close()

livros = {}
count = 0
while True:
    opcao = int(menu())

    match opcao:
        case 1:
            cadastrar()
            continue
        
        case 2:
            listar()                
            continue

        case 3:
            procurar()                
            continue
        
        case 4:
            excluir()
            continue

        case 5:
            contar()
            continue

        case 0:
            confirma = input("Realmente deseja sair? (S|N): ").upper
            if confirma == "S":
                break
            else:
                continue
            
        case _:
            print("Opção invalida!")
            continue

    break