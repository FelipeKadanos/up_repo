# DICIONARIO:
# É basicamente um array associativo

# Um dicionário armazena informações no formato:
# CHAVE -> VALOR 

participante = {
    "nome": "Carlos",
    "idade": 20,
    "cidade": "Curitiba"
}

# REMOVENDO INFORMAÇÕES
del participante["cidade"]

# PERCORRENDO UM DICIONÁRIO

# Primeira forma:
for chave in participante:
    print(chave)

# Segunda forma:
for valor in participante.values():
    print(valor)

# Terceira forma:
for chave, valor in participante.items():
    print(chave, valor)

# CADASTRANDO VÁRIOS PARTICIPANTES
participantes = []
participantes.append(participante)

participantes = [
    {
        "nome": "Carlos",
        "idade": 20,
    },
    {
        "nome": "Ana",
        "idade": 22,
    }
]

for participante in participantes:
    print("Nome:", participante["nome"])
    print("Idade:", participante["idade"])