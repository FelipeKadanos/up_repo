# Comando `shift` no Bash

O comando `shift` remove o primeiro parametro da linha de comando e desloca os demais parametros uma posicao para a esquerda.

Antes de executar `shift`, considere o comando:

```bash
./parametros.sh azul verde amarelo
```

Os parametros possuem os seguintes valores:

| Variavel | Valor |
| --- | --- |
| `$1` | `azul` |
| `$2` | `verde` |
| `$3` | `amarelo` |
| `$#` | `3` |

Depois de executar `shift`, o parametro `azul` e removido. Os valores passam a ser:

| Variavel | Valor |
| --- | --- |
| `$1` | `verde` |
| `$2` | `amarelo` |
| `$#` | `2` |

Assim, o `shift` e util para percorrer todos os parametros recebidos. No exercicio `parametros.sh`, o comando mostra o valor atual de `$1` e depois executa `shift`, fazendo o proximo parametro ocupar a posicao `$1`.

```bash
while test "$#" -gt 0
do
    echo "Parametro $NUM: $1"
    NUM=$((NUM + 1))
    shift
done
```

Tambem e possivel informar uma quantidade ao comando. Por exemplo, `shift 2` remove os dois primeiros parametros. Se nao for informada uma quantidade, `shift` remove somente um parametro.
