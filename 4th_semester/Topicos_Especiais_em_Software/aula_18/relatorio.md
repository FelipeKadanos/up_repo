# Relatorio - Analise de Dados de Saude

## Preparacao dos dados

O arquivo `Atividade2.csv` possui 5.110 registros e 12 colunas. A verificacao inicial encontrou 201 valores ausentes na coluna `bmi` e 1.544 registros com `Unknown` na coluna `smoking_status`.

Os valores ausentes de BMI foram preenchidos com a mediana da coluna, que foi 28,1. Essa medida foi escolhida porque sofre menos influencia de valores muito altos ou baixos. Os valores `Unknown` de tabagismo foram alterados para `Not informed`, deixando claro que essa informacao nao foi fornecida. Depois do tratamento, nao restaram dados ausentes nem valores `Unknown`.

## Analise dos dados

O dataset possui 249 pacientes com registro de AVC e 4.861 sem registro de AVC. As medias encontradas foram:

| Caracteristica | Sem AVC | Com AVC |
| --- | ---: | ---: |
| Idade | 41,97 | 67,73 |
| Hipertensao | 8,89% | 26,51% |
| Doenca cardiaca | 4,71% | 18,88% |
| Nivel medio de glicose | 104,80 | 132,54 |
| BMI | 28,80 | 30,09 |

Os pacientes com AVC apresentam maior idade media, maior nivel medio de glicose e maior BMI medio. A hipertensao e a doenca cardiaca tambem aparecem com maior frequencia nesse grupo.

Na comparacao do tabagismo, o grupo com AVC possui 90 pacientes que nunca fumaram, 70 que fumaram anteriormente, 42 fumantes e 47 sem informacao. Como os grupos possuem tamanhos muito diferentes, esses valores devem ser interpretados junto com a quantidade total de pacientes de cada grupo.

## Graficos

O primeiro grafico mostra a distribuicao das idades dos pacientes com AVC. O segundo compara o nivel medio de glicose dos grupos com e sem AVC. O terceiro apresenta o percentual de pacientes com hipertensao em cada grupo. A hipertensao foi escolhida porque sua frequencia e consideravelmente maior entre os pacientes com AVC neste dataset.

## Banco de dados

Os 5.110 registros tratados foram armazenados na tabela `pacientes` do banco `atividade2.db`. As consultas confirmaram 5.110 registros no total, 249 pacientes com AVC e idade media de 62,24 anos entre os pacientes com hipertensao.

## Conclusao

No conjunto analisado, o grupo com AVC apresenta idade, glicose, BMI, hipertensao e doenca cardiaca maiores que o grupo sem AVC. Esses resultados mostram associacoes presentes somente nesta base de dados. Eles nao permitem concluir que uma dessas caracteristicas seja, sozinha, a causa do AVC.
