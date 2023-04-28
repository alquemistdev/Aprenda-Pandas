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
 - Para usar o pandas bastar usar o comando:
    ```python
    import pandas as pd
    ```
 - e instânciar um dataframe por usar um csv ou json:
    ```python
    # Você pode baixar a pasta ou trocar esse caminho pelo link do github
    
    # Para csv
    df = pd.read_csv("link do arquivo")

    # Para json
    df = pd.read_json("link do arquivo")
    ```

## Principais Comandos
- Retorna dados do cabeçalho do dataframe:
    ```python
    # Retorna 5 primeiras linhas do dataframe
    df.head()

    # Retorna N primeiras linhas do dataframe
    df.head(n)
    ```
- Retorna dados do final do dataframe:
    ```python
    # Retorna 5 ultimas linhas do dataframe
    df.tail()
    
    # Retorna N ultimas linhas do dataframe
    df.tail(n)
    ```
- Selecionar colunas do dataframe:
    ```python
    # Selecionando linhas da coluna
    df['c1'].head()
    
    # Selecionando mais de uma
    df[['c1', 'c2']].head()
    
    # Selecionando uma e somente uma por notação de ponto
    df.coluna.head()
    ```

- Selecionar dados do dataframe:
    ```python
    # Selecionando primeira linha
    df.loc[0]
    
    # Selecionando o intervalo
    df.loc[0:3]
    
    # Selecionando linhas unicas
    df.loc[[1, 3, 4]]
    
    # Selecionando intervalo e coluna especifica
    df.loc[1:3, "c2"]
    
    # Selecionando intervalo e mais de uma coluna especifica
    df.loc[1:3, ["c1", "c2"]]
    
    # Selecionando intervalo e intervalo de colunas
    df.loc[1:3, "c2": "c1"]
    
    # Selecionado dois dados do 0 ao 1
    df.iloc[0:2]
    
    # Selecionado dois dados do 0 ao 1, da coluna 0 a 1
    df.iloc[0:2, 0:2]
    ```

- Ordenando dados do dataframe:
    ```python
    # Ordenando uma coluna
    df.sort_values(by=["c1"]).head()
    
    # Ordenando mais de uma coluna
    df.sort_values(by=["c1", "c2"]).head()
    
    # Ordenando uma coluna e salvando
    df.sort_values('c1', inplace=True)
    
    # Ordenando em ordem decrescente
    df.sort_values('c1', ascending=False)

    # Ordenando mais de uma em ordem crescente
    df.sort_values(['c1', 'c2'], ascending=[False, True]).head()
    ```

- Filtrar dados do dataframe:
    ```python
    # Por itens, mostrar somente eles
    df.filter(items=["c1", "c2"]).head() 
    
    # Por like, contenha valor
    df.filter(like="i").head() 
    
    # Por expressão regular
    df.filter(regex='c.')    
    df.filter(regex='.[0-9]+')
    ```
- Usando operadores para selecionar dados do dataframe:
    ```python
    # Para usar operadores logicos é necessario especificar todos
    df.loc[0:2,[True, False, True, False, False, False, False]]

    # Listar verificando se é verdadeira
    df.coluna == True 

    # Listar verificando se é verdadeira
    df[df.coluna == True].head()
    
    # Operador logico 'E' - &
    df[(df.coluna == True) & (df.valor >= 0)][['c1','c2']]

    # Operador logico 'Ou' - |
    df[(df.coluna == True) & (df.valor >= 0) & ((df.cliente == "tipo1") | (df.cliente == "tipo2"))]
    df[(df.coluna == True) & (df.valor >= 0) & (df.cliente.isin(["tipo1", "tipo2"]))]
    ```
- Agrupando dados do dataframe:
    ```python
    # Media da coluna
    df.coluna.mean()

    # Media da coluna verdadeira
    df[df.coluna == True].coluna.mean()
    # Agrupando coluna
    df[['c1','c2']].groupby(['c1']).mean()

    # Agrupando mais de uma coluna
    df[['c1', 'c3','c2']].groupby(['c3','c1']).mean()
    ```