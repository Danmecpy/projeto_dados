
import pandas as pd

def clean_data(df: pd.DataFrame):
    df = df.copy() # evitar modificar o df original

    rows_in = len(df) # contar linhas iniciais

    # exemplo de regra simples (você pode colocar suas regras reais aqui)
    df = df.drop_duplicates(subset="id")

    # normalizações básicas
    df["nome"] = df["nome"].astype("string").str.strip() # remover espaços
    df["idade"] = pd.to_numeric(df["idade"], errors="coerce") # converter para numérico
    df["salario"] = pd.to_numeric(df["salario"], errors="coerce") # converter para numérico
    df["data_cadastro"] = pd.to_datetime(df["data_cadastro"], errors="coerce") # converter para datetime

    # filtros (regras)
    df = df[df["nome"].notna() & (df["nome"] != "")] # nomes vazios
    df = df[df["idade"].between(18, 100)] # idade entre 18 e 100
    df = df[df["salario"].between(1, 100000)] # salário positivo e razoável
    df = df[df["data_cadastro"] >= "2000-01-01"]
    df = df[df["ativo"].notna()]    # remover nulos em ativo
    df = df[df["ativo"].astype(str).str.lower().isin(["true"])] # ativo como booleano
   
    rows_out = len(df)

    dq = {
        "rows_in": rows_in,
        "rows_out": rows_out,
        "rows_removed_total": rows_in - rows_out,
    }

    return df, dq





#### código abaixo removido conforme solicitado









"""def clean_data(df):
   #tirar duplicatas 
   df = df.drop_duplicates(subset=['id'])
   #tirar valores nulos
   df = df.dropna()
   #corrigir tipos de dados  
   df['idade'] = pd.to_numeric(df['idade'], errors='coerce')
   df['salario'] = pd.to_numeric(df['salario'], errors='coerce')
   df['data_cadastro'] = pd.to_datetime(df['data_cadastro'], errors='coerce')
   #Transformar True/False em boolean
   df['ativo'] = df['ativo'].astype(str).str.lower().map({'true': True, 'false': False})
   #salários negativos/zerados
   df = df[df['salario'] > 0]
   #nomes vazios
   df = df[df['nome'].str.len() > 0]
   #apenas ativos
   df = df[df['ativo'] == True]
   #datas inválidas
   df = df[(df['data_cadastro'] >= '2000-01-01')]
   #Strings sujas (None,vazias,espaços)
   df = df[~df['nome'].isin([None, '', '   ', 'N/A'])]
   #Colunas incosistentes
   df = df[df['ativo'].isin([True, False])]
    #Tipos errados (string ondde deveria ser número e vice-versa)
   df = df[pd.to_numeric(df['idade'], errors='coerce').notnull()]
   df = df[pd.to_numeric(df['salario'], errors='coerce').notnull()]
   #Idade entre 18 e 100
   df = df[(df['idade'] >= 18) & (df['idade'] <= 100)]
   return df"""