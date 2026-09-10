# EXERCICIO DE FIXACAO - LAMBDA

produtos = [
    ("Notebook", 3500),
    ("Mouse", 80),
    ("Teclado", 150),
    ("Monitor", 1200),
    ("Webcam", 250),
]


# 1. Mostre o produto mais caro.
produto_mais_caro = max(produtos, key=lambda produto: produto[1])
print("Produto mais caro:", produto_mais_caro)


# 2. Mostre o produto mais barato.
produto_mais_barato = min(produtos, key=lambda produto: produto[1])
print("Produto mais barato:", produto_mais_barato)


# 3. Ordene os produtos do mais barato para o mais caro.
produtos_ordenados = sorted(produtos, key=lambda produto: produto[1])
print("Produtos ordenados:", produtos_ordenados)


# 4. Crie uma lista contendo os precos com 10% de desconto.
precos_com_desconto = list(map(lambda produto: produto[1] * 0.90, produtos))
print("Precos com 10% de desconto:", precos_com_desconto)


# 5. Crie uma lista contendo apenas os produtos que custam mais de R$ 500,00.
produtos_acima_500 = list(filter(lambda produto: produto[1] > 500, produtos))
print("Produtos acima de R$ 500,00:", produtos_acima_500)
