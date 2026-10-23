from sklearn.linear_model import LogisticRegression

# Dados de exemplo: [idade, renda]
X = [[25, 3000], [30, 4000], [35, 5000], [40, 6000], [45, 7000]]
# Rótulos: 1 = comprou, 0 = não comprou
y = [0, 1, 1, 1, 1]

# Criar e treinar o modelo
modelo = LogisticRegression()
modelo.fit(X, y)

novo_cliente = [[38,4500]]

resultado - modelo.predict(novo_cliente)

if resultado[0] == 1:
    print("O cliente provavelmente irá comprar o produto.")
else:
    print("O cliente provavelmente não irá comprar o produto.")