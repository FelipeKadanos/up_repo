produtos = []
def cadastrar():
    produto = {
        "codigo": int(input("Código: ")),
        "nome": input("Nome: ").title(),
        "categoria": input("Categoria: ").title(),
        "preco": float(input("Preço: "))
    }
    produtos.append(produto)
    print("Produto cadastrado.")

def listar():
    if len(produtos) == 0:
        print("Nenhum produto.")
        return

    for produto in produtos:
        print("----------------------")
        print(produto["codigo"])
        print(produto["nome"])
        print(produto["categoria"])
        print(produto["preco"])

def pesquisar():
    codigo = int(input("Código: "))
    
    for produto in produtos:
        if produto["codigo"] == codigo:
            print(produto)