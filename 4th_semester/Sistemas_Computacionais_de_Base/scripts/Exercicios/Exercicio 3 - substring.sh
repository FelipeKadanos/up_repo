#!/bin/bash

# Exercicio 3 - substring.sh

# Encerra o script se a primeira palavra nao foi recebida.
test "$1" = "" && exit

# Encerra o script se a segunda palavra nao foi recebida.
test "$2" = "" && exit

# Procura a primeira palavra dentro da segunda palavra.
echo "$2" | grep -q "$1"

# Mostra a mensagem somente quando a primeira palavra foi encontrada.
test $? -eq 0 && echo "$1 esta contida em $2"
