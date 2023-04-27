# Aprenda Pandas

## Documentação Pandas
https://pandas.pydata.org/

## Instalação Pandas
1. Sem virtualenv:
```bash
pip install pandas
```
2. Com virtualenv:
```bash
python -m virtualenv env
. env/Scripts/activate
pip install pandas
```

## Importando Pandas
Para usar o pandas bastar usar o comando:
```python
import pandas as pd
```
e instânciar um dataframe por usar um csv ou json:
```python
# Você pode baixar a pasta ou trocar esse caminho pelo link do github
df = pd.read_csv("link do arquivo", encoding="UTF-8", sep=",")
```

## Principais Comandos
```python
df.head()
```