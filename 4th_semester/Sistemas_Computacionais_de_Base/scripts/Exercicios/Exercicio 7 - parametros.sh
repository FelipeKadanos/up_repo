#!/bin/bash

# Exercicio 7 - parametros.sh

# Guarda a posicao do parametro que sera mostrado.
NUM=1

# Repete enquanto existir pelo menos um parametro.
while test "$#" -gt 0
do
    # Mostra a posicao e o parametro atual.
    echo "Parametro $NUM: $1"

    # Avanca para o proximo numero de parametro.
    NUM=$((NUM + 1))

    # Remove o parametro atual da lista de parametros.
    shift
done
