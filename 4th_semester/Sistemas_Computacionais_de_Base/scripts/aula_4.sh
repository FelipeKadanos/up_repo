#!/bin/bash
echo "-------------------------------------------------"
echo -n "Digite o nome do aquivo ou diretorio: "
read ARQUIVO

test -d "$ARQUIVO" && echo "$ARQUIVO é um diretorio!"
test -f "$ARQUIVO" && echo "$ARQUIVO é um arquivo!"
test -f "$ARQUIVO" -o -d "$ARQUIVO" || echo "O arquivo ou diretorio
         $ARQUIVO não existe!"
echo
echo "-------------------------------------------------"


# ARGUMENTOS:
# nome script: ./argumentos.sh

echo "-------------------------------------------------"
echo "Nome do desse script: $0"
echo "Recebidos $# argumentos: $*"
echo "O primeiro argumento é: $1"
echo "O segundo argumento é: $2"
echo "O terceiro argumento é: $3"
echo "O quarto argumento é: $4"
echo "O quinto argumento é: $5"
echo "-------------------------------------------------"

# OUTROS SCRIPTS:
echo "-------------------------------------------------"
echo -n "Digite o primeiro numero: "
read NUM1
echo -n "Digite o segundo numero: "
read NUM2


if test "$NUM1" -gt "$NUM2"
then
    echo
    echo "$NUM1 é maior que $NUM2"
elif test "$NUM1" -eq "$NUM2"
then
    echo
    echo "$NUM1 é igual a $NUM2"
else
    echo
    echo "$NUM1 é menor que $NUM2"
fi
echo "-------------------------------------------------"

echo "-------------------------------------------------"
for numero in um dois tres quatro cinco seis sete oito nove dez
do
    echo "Contando: $numero"
done
echo "-------------------------------------------------"

echo "-------------------------------------------------"
echo -n "Digite um numero: "
read NUM
i=0
while test $i -le $NUM
do
    echo "Contando: $i"
    i=$((i + 1))
done
echo "-------------------------------------------------"