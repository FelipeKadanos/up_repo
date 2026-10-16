# Relatorio - Analise de Dados de Saude

**Autores:** Felipe Kadanos e Marcos Ferrari

## Preparacao dos dados

O arquivo `Atividade2.csv` possui 5.110 registros e 12 colunas. A verificacao inicial encontrou 201 valores ausentes na coluna `bmi` e 1.544 registros com `Unknown` na coluna `smoking_status`.

Os valores ausentes de BMI foram preenchidos com a mediana da coluna, que foi 28,1. Essa medida foi escolhida porque sofre menos influencia de valores muito altos ou baixos. Depois do tratamento, nao restaram valores nulos identificados pelo Pandas. Os 1.544 casos `Unknown` foram mantidos: representam informacao de tabagismo nao fornecida. Como `Unknown` e uma categoria de texto, ela nao e contada como valor nulo; isso nao significa que a informacao passou a ser conhecida.

## Analise dos dados

O dataset possui 249 pacientes com registro de AVC (`stroke = 1`) e 4.861 sem registro de AVC (`stroke = 0`). As medias e os percentuais encontrados foram:

| Caracteristica | Sem AVC | Com AVC |
| --- | ---: | ---: |
| Idade media (anos) | 41,97 | 67,73 |
| Pacientes com hipertensao | 8,89% | 26,51% |
| Pacientes com doenca cardiaca | 4,71% | 18,88% |
| Nivel medio de glicose | 104,80 | 132,54 |
| BMI medio (IMC) | 28,80 | 30,09 |

Como hipertensao e doenca cardiaca sao representadas por 0 e 1, a media dessas colunas corresponde a proporcao de pacientes com a condicao. Multiplicamos essa proporcao por 100 para apresentar os percentuais. Os valores sao arredondados apenas na apresentacao.

Os pacientes com AVC apresentam maior idade media, maior nivel medio de glicose e maior BMI medio. A hipertensao e a doenca cardiaca tambem aparecem com maior frequencia nesse grupo.

Na comparacao do tabagismo, o grupo com AVC possui 90 pacientes que nunca fumaram, 70 que fumaram anteriormente, 42 fumantes e 47 sem informacao. Como os grupos possuem tamanhos diferentes, dividimos as contagens pelo total de pacientes de cada grupo e multiplicamos por 100. Os casos `Unknown` tambem fazem parte desse total.

| Situacao de tabagismo | Sem AVC (4.861 pacientes) | Com AVC (249 pacientes) |
| --- | ---: | ---: |
| Nunca fumou (`never smoked`) | 37,07% | 36,14% |
| Ex-fumante (`formerly smoked`) | 16,77% | 28,11% |
| Fuma (`smokes`) | 15,37% | 16,87% |
| Nao informado (`Unknown`) | 30,80% | 18,88% |

A proporcao de ex-fumantes e maior no grupo com AVC, enquanto a proporcao de quem nunca fumou e semelhante nos dois grupos. Os casos sem informacao tambem tem proporcoes diferentes, o que limita a interpretacao. Esses resultados descrevem o dataset e nao demonstram que o tabagismo causou os casos de AVC. Os percentuais somam aproximadamente 100% em cada coluna; pequenas diferencas ocorrem pelo arredondamento.

## Graficos

O primeiro grafico mostra a distribuicao das idades dos pacientes com AVC. O segundo compara o nivel medio de glicose dos grupos com e sem AVC. O terceiro apresenta o percentual de pacientes com hipertensao em cada grupo. A hipertensao foi escolhida porque sua frequencia e consideravelmente maior entre os pacientes com AVC neste dataset.

## Banco de dados

Os 5.110 registros tratados foram armazenados na tabela `pacientes` do banco `atividade2.db`. O metodo `to_sql` do Pandas cria a tabela e grava os dados. A opcao `if_exists="replace"` recria a tabela a cada execucao para evitar duplicacao, e `index=False` impede a gravacao do indice do DataFrame como uma coluna adicional. Os nomes das 12 colunas sao preservados, incluindo `Residence_type`. A coluna `id` e armazenada como uma coluna comum, sem restricao de chave primaria.

O codigo executa quatro consultas SQL para atender aos tres tipos de consulta pedidos no enunciado:

1. `COUNT(*)` conta todos os registros: **5.110 pacientes**.
2. `COUNT(*)` com `WHERE stroke = 1` conta os pacientes com AVC: **249 pacientes**.
3. `SELECT *` com `WHERE stroke = 1 LIMIT 5` busca **cinco exemplos de pacientes com AVC**, recuperados com `fetchall()`. Essa consulta nao busca todos os 249 registros nem define uma ordenacao.
4. `ROUND(AVG(age), 2)` com `WHERE hypertension = 1` calcula a idade media dos hipertensos: **62,24 anos**.

Na revisao, os dados do banco foram comparados com o CSV apos o preenchimento do BMI. Os registros coincidem, e os 5.110 IDs sao unicos.

## Conclusao

No conjunto analisado, o grupo com AVC apresenta maiores medias de idade, glicose e BMI, alem de maiores percentuais de hipertensao e doenca cardiaca. Tambem ha maior proporcao de ex-fumantes nesse grupo.

Esses resultados mostram associacoes observadas nesta base de dados. O preenchimento do BMI pela mediana nao recupera os valores reais ausentes, e os casos de tabagismo nao informado limitam a interpretacao dessa caracteristica. As diferencas encontradas nao permitem concluir que uma dessas caracteristicas seja a causa do AVC.
