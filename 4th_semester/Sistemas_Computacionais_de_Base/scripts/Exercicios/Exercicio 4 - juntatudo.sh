#!/bin/bash

# Exercicio 4 - juntatudo.sh

# Junta os parametros e remove os espacos entre eles.
echo "$*" | tr -d ' '
