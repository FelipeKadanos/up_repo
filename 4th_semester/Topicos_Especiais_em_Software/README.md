# Tópicos Especiais em Software

Arquivos e exercícios da disciplina, organizados em pastas por aula. O ambiente virtual Python fica em `.venv`, na raiz de `Topicos_Especiais_em_Software`, e pode ser usado por todas as aulas.

Os comandos abaixo são para o **PowerShell no Windows**.

## Ativar o ambiente virtual

Se o terminal estiver na pasta `Topicos_Especiais_em_Software`:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se estiver dentro de uma pasta de aula, como `aula_20`:

```powershell
..\.venv\Scripts\Activate.ps1
```

Depois da ativação, o terminal normalmente exibe `(.venv)` antes do caminho. Você pode navegar entre as pastas e continuar usando o mesmo ambiente. A ativação vale apenas para o terminal atual; repita-a ao abrir outro terminal.

Para conferir qual Python está sendo usado:

```powershell
python -c "import sys; print(sys.executable)"
```

O caminho deve terminar em `Topicos_Especiais_em_Software\.venv\Scripts\python.exe`.

## Executar uma aula

Com o ambiente ativo, entre na pasta da aula e execute o arquivo. Partindo de `Topicos_Especiais_em_Software`:

```powershell
cd aula_20
python aula_20.py
```

Se você já estiver em `aula_20`, basta executar `python aula_20.py`.

Também é possível executar um arquivo a partir da raiz da disciplina:

```powershell
python .\aula_20\aula_20.py
```

Prefira executar dentro da pasta da aula quando o programa lê ou grava arquivos usando caminhos relativos: esses caminhos dependem da pasta atual do terminal.

## Instalar pacotes

Com o ambiente ativo, use `python -m pip install` seguido do nome do pacote. Por exemplo, para instalar as bibliotecas usadas na aula 20:

```powershell
python -m pip install requests beautifulsoup4
```

O pacote `beautifulsoup4` é importado no código como `bs4`.

Se um trabalho tiver um arquivo `requirements.txt`, instale as dependências dele. Exemplo, a partir da raiz da disciplina:

```powershell
python -m pip install -r .\aula_18\trab_2\requirements.txt
```

As bibliotecas instaladas nesse ambiente ficam disponíveis para todas as aulas que o utilizarem. Consulte também as [instruções do trabalho 2](aula_18/trab_2/README.md).

## Usar sem ativar o ambiente

Você pode chamar o executável diretamente. A partir de `Topicos_Especiais_em_Software`:

```powershell
.\.venv\Scripts\python.exe .\aula_20\aula_20.py
.\.venv\Scripts\python.exe -m pip install requests
```

## Desativar o ambiente

```powershell
deactivate
```

## Criar o ambiente em outra máquina

Com o Python instalado e disponível no terminal, execute na pasta `Topicos_Especiais_em_Software`, caso ainda não exista uma `.venv`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Depois, instale as dependências necessárias para a aula ou trabalho. O ambiente virtual é local e deve ser recriado em cada máquina.
