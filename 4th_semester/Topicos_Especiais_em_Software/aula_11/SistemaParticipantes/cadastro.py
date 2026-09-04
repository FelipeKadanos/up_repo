from participante import Participante
from dados import participantes


def cadastrar():

    print("\n===== CADASTRO DE PARTICIPANTE =====")

    nome = input("Nome: ").strip().title()
    email = input("Email: ").strip().title()
    categoria = input("Categoria (ESTUDANTE | PROFISSIONAL | PALESTRANTE): ").strip().upper()

    if categoria == "ESTUDANTE" or categoria == "PROFISSIONAL" or categoria == "PALESTRANTE":
        categoria = categoria
    else:
        print("\nCategoria inválida.")
        return

    try:
        idade = int(input("Idade: "))
        valor_pago = float(input("Valor pago: R$ "))
    except ValueError:
        print("\nIdade ou valor pago inválido.")
        return

    if idade <= 0:
        print("\nIdade inválido.")
        return

    if valor_pago < 0:
        print("\nValor pago inválido.")
        return

    participante = Participante(
        nome,
        idade,
        email,
        categoria,
        valor_pago
    )

    participantes.append(participante)
    print("\nParticipante cadastrado com sucesso!")

def listar():
    if len(participantes) == 0:
        print("\nNenhum participante cadastrado.")
        return

    print("\n========== PARTICIPANTES ==========")

    for participante in participantes:
        participante.mostrar_dados()


def procurar():
    if len(participantes) == 0:
        print("\nNenhum participante cadastrado.")
        return

    nome = input("\nNome do participante: ").strip().title()
    encontrado = False

    for participante in participantes:
        if participante.nome == nome:
            print("\nParticipante encontrado!")
            participante.mostrar_dados()
            encontrado = True
            break

    if not encontrado:
        print("\nParticipante não encontrado.")

def alterar():
    nome = input("\nNome do participante: ").strip().title()
    encontrado = False

    for participante in participantes:
        if participante.nome == nome:
            encontrado = True
            print("\nParticipante encontrado.")
            participante.mostrar_dados()

            try:
                nova_idade = int(input("Idade: "))
                novo_valor_pago = float(input("Valor pago: R$ "))
            except ValueError:
                print("\nIdade ou valor pago inválido.")
                return
                
            if nova_idade <= 0:
                print("\nIdade inválido.")
                return

            if novo_valor_pago < 0:
                print("\nValor pago inválido.")
                return

            nova_categoria = input("Categoria (ESTUDANTE | PROFISSIONAL | PALESTRANTE): ").strip().upper()

            if nova_categoria == "ESTUDANTE" or nova_categoria == "PROFISSIONAL" or nova_categoria == "PALESTRANTE":
                nova_categoria = nova_categoria
            else:
                print("\nCategoria inválida.")
                return              

            participante.categoria = nova_categoria
            participante.idade = nova_idade
            participante.valor_pago = novo_valor_pago
            print("\nAlteração concluída.")
            break

    if not encontrado:
        print("\nParticipante não encontrado.")

def excluir():
    nome = input("\nNome do participante: ").strip().title()
    encontrado = False

    for participante in participantes:
        if participante.nome == nome:
            participantes.remove(participante)
            print("\nParticipante excluído com sucesso.")
            encontrado = True
            break

    if not encontrado:
        print("\nParticipante não encontrado.")


def estatisticas():
    if len(participantes) == 0:
        print("\nNenhum participante cadastrado.")
        return

    total_participantes = len(participantes)
    
    participante_mais_velho = participantes[0]
    participante_mais_novo = participantes[0]
    soma_idade = 0
    est = 0
    prof = 0
    palestrantes = 0
    soma_valor_pago = 0

    for participante in participantes:

        if participante.categoria == "ESTUDANTE":
            est += 1
        elif participante.categoria == "PROFISSIONAL":
            prof += 1
        else:
            palestrantes += 1

        soma_idade += participante.idade
    
        if participante.idade > participante_mais_velho.idade:
            participante_mais_velho = participante

        if participante.idade < participante_mais_novo.idade:
            participante_mais_novo = participante

        soma_valor_pago += participante.valor_pago


    media = soma_idade / total_participantes

    print("\n========== ESTATÍSTICAS ==========")
    print("Total de participantes:", total_participantes)
    print("Quantidade de estudantes: ", est)
    print("Quantidade de profissionais: ", prof)
    print("Quantidade de palestrantes: ", palestrantes)
    print("Média de idade dos participantes: ", media)
    # print("Participante mais velho: ") 
    # participante_mais_velho.mostrar_dados()
    # print("Participante mais novo: ") 
    # participante_mais_novo.mostrar_dados()

    print("\nParticipante mais velho:",participante_mais_velho.nome)
    print("Idade: ",participante_mais_velho.idade)
    print("\nParticipante mais novo:",participante_mais_novo.nome)
    print("Idade: ",participante_mais_novo.idade)
    
    print("Total arrecadado: R$", round(soma_valor_pago, 2))