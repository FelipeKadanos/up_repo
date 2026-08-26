# Anotações da aula de scripts

# Se o arquivos não estiver em $PATH precisamso utilizar ./ no inicio do comando para poder executar o script.
./nome_do_script.sh bash

# Caso o arquivo não esteja no diretório atual, podemos utilizar o comando inteiro para executar o script:
/home/usuario/scripts/nome_do_script.sh bash

# Podemos escrever um arquivo utilizando o nano:
nano nome_do_script.sh

# Todo script precisa ter no inicio: 
#!/bin/bash

# Exemplo de script que mostra a data, o espaço em disco e os usuários logados no sistema:
#!/bin/bash
date
df
w

# Todo script precisa ter permissão de executação.
chmod +x nome_do_script.sh

# O comando "echo" serve para imprimir mensagens ou qualquer tipo de informação na tela:
echo 
echo "Olá, mundo!"

# INTERAÇÃO COM O USUÁRIO:
#!/bin/bash
echo "Digite seu nome:"
read nome
test "$nome" = "" && echo "Você não digitou nada!" && exit 
echo "Olá, $nome!"

echo
echo "Vou buscar os dados do sistema. Posso continuar? (s/n)"
read RESP
test "$RESP" = "n" && exit 

echo
echo "Data e hora do sistema: "

date

echo
echo "Utilização do armazenamento: "

df

echo
echo "Usuario atual: "

w

echo

# É possivel utilizar variaveis na linha de comando, por exemplo:

HOJE=$(date +%d/%m/%Y)
echo "Hoje é $HOJE"
unset HOJE
echo HOJE

# Variáveis de ambiente:
env

# NAME=Hardness
# WSL_DISTRO_NAME=Ubuntu-20.04
# SHELL=/bin/bash

# Comandos:

man # Mostra o manual do comando.
ls -l # Lista os arquivos do diretório atual com detalhes.
grep -i "palavra" arquivo.txt # Procura a palavra no arquivo.txt, ignorando maiúsculas e minúsculas.
cat -n arquivo.txt # Mostra o conteúdo do arquivo.txt com numeração de linhas.

cat /etc/passwd # Mostra o conteúdo do arquivo passwd, que contém informações sobre os usuários do sistema.
cat /etc/passwd | grep -i "root" # Mostra as informações do usuário root no arquivo passwd.
cat /etc/passwd | grep -i "root" | cut -c1-30 # Mostra os 30 primeiros caracteres da linha que contém a palavra root no arquivo passwd.

cat /etc/passwd | grep -i "root" | cut -c1-30 > arquivo.txt # Salva os 30 primeiros caracteres da linha que contém a palavra root no arquivo passwd em um novo arquivo chamado arquivo.txt.
more arquivo.txt # Mostra o conteúdo do arquivo.txt uma página por vez.

# Comando "test"
test -f arquivo.txt && echo "O arquivo existe" || echo "O arquivo não existe" # Verifica se o arquivo existe.