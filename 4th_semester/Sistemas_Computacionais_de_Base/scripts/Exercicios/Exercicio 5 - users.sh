#!/bin/bash

# Exercicio 5 - users.sh

# Mostra os campos usuario e nome completo do arquivo de usuarios.
cut -d ':' -f 1,5 /etc/passwd | tr ':' '\t'
