# ARQUIVO
arquivo = open("livros.txt","w")

# r Leitura
# w Escrita
# a Acrescentar
# x Criar novo arquivo

arquivo = open("livros.txt","w")
arquivo = write("teste")
arquivo.close()

# ESCREVENDO VARIAS LINHAS
arquivo = open("livros.txt","w")
arquivo.write("Dom Casmurro\n")
arquivo.write("O Cortiço\n")
arquivo.write("Capitães da Areia\n")
arquivo.close()


# LENDO UM ARQUIVO
arquivo = open("livros.txt","r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()


# ACRESCENTANDO INFORMAÇÕES
arquivo = open("livros.txt","a")
arquivo.write("\nPython para Engenharia")
arquivo.close()


# WITH OPEN()
with open("livros.txt","r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)

# Quando o bloco termina, o python fecha o arquivo automaticamente, sem necessidade de usar o close().

# LENDO LINHA POR LINHA
with open("livros.txt","r") as arquivo:
    for linha in arquivo:
        
print(linha)