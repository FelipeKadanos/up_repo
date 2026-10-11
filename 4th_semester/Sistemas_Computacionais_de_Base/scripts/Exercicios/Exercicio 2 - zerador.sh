#!/bin/bash

# Exercicio 2 - zerador.sh

# Guarda o numero recebido para fazer a contagem regressiva.
NUM=$1

# Repete enquanto o numero for maior ou igual a zero.
while test "$NUM" -ge 0
do
    # Mostra o numero sem pular para a proxima linha.
    echo -n "$NUM "

    # Diminui um do numero atual.
    NUM=$((NUM - 1))
done

# Pula para a proxima linha ao terminar a contagem.
echo
