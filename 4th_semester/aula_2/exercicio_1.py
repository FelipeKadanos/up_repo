nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
ing = input("Digite seu tipo de ingresso (VIP/COMUM): ")

if idade <= 16:
    print("Entrada negada. A entrada é permitida apenas para maiores de 16 anos")
    exit()
    
if ing.upper() == "VIP":
    print("Você tem acesso a área VIP!")
elif ing.upper() == "COMUM":
    print("Você tem acesso a área COMUM.")
else:
    print("Você não tem um ingresso disponível.")