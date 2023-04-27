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
```python
import pandas as pd
```
lendo um arquivo csv 
```python
# Você pode baixar a pasta ou trocar esse caminho pelo link do github
df = pd.read_csv("data/minecraft.csv", encoding="UTF-8", sep=",")
```

## Principais Comandos
```python
df.head()
```