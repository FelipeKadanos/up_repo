## Equipes de no máximo 4 alunos.

### Análise de Dados de Saúde

> A análise de dados é uma importante ferramenta para compreender características de uma população e identificar padrões que podem auxiliar estudos e tomadas de decisão.

Neste trabalho, será utilizado o arquivo `Atividade2.csv`, que contém informações demográficas e indicadores de saúde de pacientes, incluindo idade, gênero, hipertensão, doença cardíaca, nível médio de glicose, IMC, tabagismo e registro de ocorrência de AVC.

O objetivo do trabalho é desenvolver, em Python, uma análise dos dados utilizando os recursos estudados durante a disciplina.



### 1. Preparação e limpeza dos dados
Carregue o arquivo fornecido e realize uma análise inicial da base de dados.

O programa deverá identificar a quantidade de registros e as características disponíveis no dataset, verificar a existência de dados ausentes e realizar o tratamento adequado quando necessário.

Ao final desta etapa, apresente evidências de que os dados foram tratados.



### 2. Análise dos dados

Realize uma análise exploratória comparando os pacientes **com e sem registro de AVC**.

A análise deverá considerar, no mínimo:
* idade;
* hipertensão;
* doença cardíaca;
* nível médio de glicose;
* IMC;
* situação de tabagismo.

A equipe deverá utilizar filtros, cálculos estatísticos e agrupamentos para identificar diferenças e características observadas entre os grupos.

Não basta apenas apresentar os dados: a equipe deverá `explicar o que os resultados encontrados representam dentro do conjunto de dados analisado.`



### 3. Visualização dos dados

Utilizando **Matplotlib**, produza **três gráficos** que auxiliem na compreensão dos dados.

Dois gráficos serão obrigatórios:

> Gráfico 1 – Distribuição das idades dos pacientes com registro de AVC

Apresente graficamente como as idades estão distribuídas entre os pacientes que possuem stroke = 1.

> Gráfico 2 – Comparação entre pacientes com e sem AVC

Escolha uma das seguintes características e construa um gráfico que permita comparar os dois grupos:

* hipertensão;
* doença cardíaca;
* nível médio de glicose;
* IMC;
* tabagismo.

>Gráfico 3 – Análise livre

A equipe deverá escolher uma informação do dataset que considere relevante, produzir uma visualização e justificar a escolha.

Todos os gráficos deverão apresentar **título, identificação adequada dos eixos e rótulos legíveis.**



### 4. Persistência dos dados – SQLite

Após a preparação dos dados, armazene as informações tratadas em um banco de dados SQLite.

O programa deverá:

* criar o banco de dados;
* criar uma tabela adequada para armazenar os registros;
* inserir os dados tratados;
* realizar consultas ao banco.

Deverão ser apresentadas pelo menos três consultas, sendo obrigatoriamente:

1. quantidade total de registros armazenados;
2. pacientes com registro de AVC;
3. uma consulta definida pela própria equipe envolvendo pelo menos uma das características analisadas no trabalho.


## Entrega
A equipe deverá entregar:

* arquivo(s) Python (.py);
* arquivo CSV utilizado;
* banco de dados SQLite (.db);
* gráficos produzidos;
* um pequeno relatório contendo os principais resultados e conclusões da análise.
O programa deverá executar corretamente utilizando os arquivos entregues.



## Observação importante
Os resultados encontrados devem ser interpretados **com base no dataset fornecido**. Uma diferença observada entre os pacientes com e sem registro de AVC não significa, por si só, que determinada característica seja a causa do AVC.



## Critérios de avaliação

| Critério  | Valor |
| :-------------: |-------------:|
| Preparação e limpeza dos dados | 0,30 |
| Análise dos dados | 0,40 |
| Visualização com Matplotlib | 0,40 |
| Persistência e consultas SQLite | 0,30 |
| Total | 1,50 |