from cadastro import produtos

def salvar():
    with open("produtos.txt","w") as arquivo:
        for produto in produtos:
            linha = (
                f'{produto["codigo"]};'
                f'{produto["nome"]};'
                f'{produto["categoria"]};'
                f'{produto["preco"]}\n'
            )
            arquivo.write(linha)
            print("Arquivo salvo.")

def carregar():
    produtos.clear()
    with open("produtos.txt","r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            produto = {
                "codigo": int(dados[0]),
                "nome": dados[1],
                "categoria": dados[2],
                "preco": float(dados[3])
            }
            produtos.append(produto)
    print("Arquivo carregado.")