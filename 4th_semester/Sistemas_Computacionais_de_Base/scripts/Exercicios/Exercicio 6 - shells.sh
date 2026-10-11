#!/bin/bash

# Exercicio 6 - shells.sh

# Seleciona o ultimo campo de cada linha do arquivo de usuarios.
cut -d ':' -f 7 /etc/passwd |
# Ordena os shells para que linhas iguais fiquem juntas.
sort |
# Remove os shells repetidos.
uniq
