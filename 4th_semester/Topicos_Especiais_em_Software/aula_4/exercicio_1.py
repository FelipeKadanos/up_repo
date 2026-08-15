cidades = []
count = 0
while True:
    print("=" * 30)
    print("SISTEMA DE CADASTRO DE CIDADES")
    print("=" * 30)

    opcao = int(input"""\n
        1 - Cadastrar cidade
        2 - Listar cidades
        3 - Procurar cidades
        4 - Excluir cidade
        5 - Ordenar cidades
        6 - Limpar cadastro
        0 - Sair
        Digite a opção que deseja: """)

    match opcao:
        case 1:
            cidades[count] = input(f"Nome da cidade: {count + 1}").strip().title()
            continue
        
        case 2:
            print("Cidades incluidas: ")
            for cidade in cidades:
                print(cidade)
                
            continue

        case 3:
            procura = input("Digite a cidade que deseja: ").strip().title()
            if procura in cidades:
                print("Encontrado!")
            else:
                print("Não encontrada!")
                
            continue
        
        case 4:
            exclui = input("Digite a cidade que deseja excluir: ").strip().title()
            if cidades.remove(exclui) == True:
                print("Cidade removida")
            else:
                print("Cidade não encontrada!")

            continue

        case 5:
            ordem = int(input("1 - Ordem alfabetica | 2- Ordem alfabetica invertida: "))
            if ordem == 2:
                if cidades.sort(reverse=True) == True:
                    print("Cidades ordenadas em ordem alfabetica invertida.")
                else:
                    print("Ordenação não realizada!")
            else:
                if cidades.sort() == True:
                    print("Cidades ordenadas em ordem alfabetica.")
                else:
                    print("Ordenação não realizada!")

            continue

        case 6:
            confirma = input("Realmente deseja limpar cadastros? (S|N): ").upper
            if confirma == "S":
                if cidades.clear() == True:
                    print("Cadastro limpo!")
                else:
                    print("Não foi possivel limpar cadastro")
            else:
                print("Operação não realizada!")

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