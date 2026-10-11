#!/bin/bash

# Exercicio 1 - relacao.sh

# Compara o primeiro numero com o segundo numero recebido.
if test "$1" -gt "$2"
then
    # Mostra que o primeiro numero e maior.
    echo "$1 e maior que $2"
elif test "$1" -eq "$2"
then
    # Mostra que os dois numeros sao iguais.
    echo "$1 e igual a $2"
else
    # Mostra que o primeiro numero e menor.
    echo "$1 e menor que $2"
fi
