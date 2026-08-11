nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print("O valor da sua mensalidade é: ")

if idade < 18:
    print("R$ 70,00")
elif idade < 40:
    print("R$ 120,00")
elif idade < 60:
    print("R$ 90,00")
else:
    print("R$ 60,00")