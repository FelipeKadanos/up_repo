while True:
    print("=" * 40)
    print("\t\tEVENTO TECH 2026")
    print("=" * 40)

    opcao = int(input"""\n
        1 - Nova inscrição
        2 - Consultar inscrição
        3 - Alterar nome
        4 - Sair
        Digite a opção que deseja: """)

    match opcao:
        case 1:
            nome = input("Nome do participante: ").strip().title()
            cidade = input("Cidade do participante: ").strip().title()
            idade = int(input("Idade do participante: "))

            if idade < 16:
                status = "Incrição negada!"
            elif idade < 18:
                status = "Necessita autorização."
            else:
                status = "Inscrição autorizada!"

            print(status)
            continue
        
        case 2:
            print(nome)
            print(cidade)
            print(idade)
            print(status)
            continue

        case 3:
            nome = input("Digite o novo nome: ").strip().title()
            print("Nome alterado com sucesso!")
            continue
        
        case 4:
            print("Saindo...")
        case _:
            print("Opção invalida!")
            continue

    break
