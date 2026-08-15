livros = {}
count = 0
while True:
    print("=" * 30)
    print("SISTEMA DE CADASTRO DE LIVROS")
    print("=" * 30)

    opcao = int(input("\n1 - Cadastrar \n2 - Listar \n3 - Procurar \n4 - Excluir \n5 - Quantidade \n0 - Sair \nDigite a opção que deseja: "))

    match opcao:
        case 1:
            livro = {}
            print("Livro ", count + 1)

            livro["nome"] = nome = input(f"Nome do livro:").strip().title()
            livro[nome]["autor"] = input(f"Autor:").strip().title()
            livro[nome]["ano"] = input(f"Ano:").strip().title()
            livro[nome]["editora"] = input(f"Editora:").strip().title()

            livros.append(livro)
            count += 1

            continue
        
        case 2:
            print("Livros incluidos: ")
            
            for livro in livros:
                print(livro)
                
                for chave, valor in livro.items():
                    print(chave, valor)
                
            continue

        case 3:
            procura = input("Digite o livro que deseja: ").strip().title()

            if procura in livros:
                print("Encontrado!")
                print(livros[procura])

                for chave, valor in livros[procura].items():
                    print(chave, valor)
            else:
                print("Não encontrado!")
                
            continue
        
        case 4:
            exclui = input("Digite o nome do livro que deseja excluir: ").strip().title()
            encontrado = False

            for livro in livros:
                if livro.get("nome") == exclui:
                    livros.remove(livro)
                    print("Livro removido!")
                    encontrado = True
                    break
            
            if not encontrado:
                print("Livro não encontrado!")

            continue

        case 5:
            qtd = 0

            for livro in livros:
                qtd += 1 

            print("quantidade de livros: ", qtd)

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