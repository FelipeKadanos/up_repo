# Trabalho 2 — Análise de Dados de Saúde

**Disciplina:** Tópicos Especiais em Software — Aula 18  
**Autores:** Felipe Kadanos e Marcos Ferrari

Análise do arquivo `Atividade2.csv` para comparar pacientes com e sem registro de AVC. O programa trata valores ausentes de IMC (BMI), apresenta estatísticas, produz três gráficos e armazena os dados tratados em SQLite.

O [enunciado](trab_2.md) contém os requisitos da atividade. O [relatório](relatorio.md) apresenta os resultados e suas interpretações.

## Instalar o Python 3.11 no Windows

1. Acesse a [página oficial do Python 3.11.9](https://www.python.org/downloads/release/python-3119/) e, na tabela **Files**, baixe **Windows installer (64-bit)** para um computador Windows x64.
2. Abra o instalador, marque **Add python.exe to PATH** e mantenha a instalação do **Python Launcher** habilitada. Clique em **Install Now**.
3. Abra um novo PowerShell e confira a versão:

```powershell
py -3.11 --version
```

O resultado deve começar com `Python 3.11`. O comando `py -3.11` seleciona essa versão mesmo quando há outras instaladas. Mais detalhes estão na [documentação oficial para Windows](https://docs.python.org/3.11/using/windows.html).

## Preparar o projeto

Se o terminal já estiver nessa pasta, continue com os comandos abaixo. Crie um ambiente virtual para o projeto e instale as dependências:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Esses comandos usam diretamente o Python do ambiente, sem precisar ativá-lo no PowerShell. Em outro computador, crie o ambiente novamente em vez de copiar a pasta `.venv`.

O `requirements.txt` contém:

| Biblioteca | Uso |
| --- | --- |
| pandas | Leitura do CSV, tratamento, análise e gravação dos dados no banco. |
| matplotlib | Criação dos gráficos. |
| numpy | Suporte numérico utilizado pelas bibliotecas; não é importado diretamente pelo script. |

Os módulos `os` e `sqlite3` já fazem parte do Python.

## Executar

Com o terminal na pasta do trabalho, execute:

```powershell
.\.venv\Scripts\python.exe .\trab_2.py
```

Mantenha `Atividade2.csv` na mesma pasta de `trab_2.py`. O programa resolve os caminhos a partir da localização do script.

O terminal mostrará a preparação dos dados, a comparação dos grupos, as contagens e os percentuais de tabagismo e os resultados das consultas SQL. Para o CSV fornecido, os principais valores são:

| Verificação | Resultado esperado |
| --- | ---: |
| Registros e colunas | 5.110 registros e 12 colunas |
| Valores de BMI ausentes antes do tratamento | 201 |
| Mediana usada no preenchimento | 28,1 |
| Valores nulos após o tratamento | 0 |
| Tabagismo não informado (`Unknown`), mantido como categoria | 1.544 |
| Pacientes com / sem AVC | 249 / 4.861 |
| Idade média dos pacientes com hipertensão | 62,24 anos |

Os três gráficos são salvos em PNG na pasta do trabalho. O modo `Agg` do Matplotlib permite salvá-los sem abrir uma janela; abra os arquivos para visualizá-los.

A cada execução, a tabela `pacientes` é recriada com os dados tratados e os gráficos são sobrescritos. O CSV original permanece intacto.

## Arquivos

| Arquivo | Finalidade |
| --- | --- |
| `trab_2.py` | Programa principal. |
| `Atividade2.csv` | Dados originais usados na análise. |
| `atividade2.db` | Banco SQLite gerado, com a tabela `pacientes`. |
| `grafico_1_idades_avc.png` | Histograma das idades dos pacientes com AVC. |
| `grafico_2_glicose.png` | Comparação da glicose média entre os grupos. |
| `grafico_3_hipertensao.png` | Comparação do percentual de hipertensão entre os grupos. |
| `relatorio.md` | Resultados e conclusões da análise. |
| `trab_2.md` | Enunciado da atividade. |
| `requirements.txt` | Dependências para instalação. |

## Organização do código

- `preparar_dados()`: lê o CSV, verifica ausências e preenche o BMI pela mediana. Mantém `Unknown` como informação de tabagismo não fornecida.
- `analisar_dados(dados)`: compara os grupos, exibe médias e percentuais e retorna as médias sem arredondamento para os gráficos.
- `criar_graficos(dados, medias)`: gera o histograma e os dois gráficos de barras.
- `salvar_banco(dados)`: grava os dados com `to_sql` e executa quatro consultas: total de registros, total com AVC, até cinco exemplos com AVC e idade média dos hipertensos.
- `main()`: chama as quatro etapas na ordem de execução.

As diferenças encontradas descrevem este conjunto de dados e não demonstram relações de causa e efeito.
