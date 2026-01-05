path = "C:\\Users\\danme\\projeto_dados\\data\\raw\\dados_brutos.csv"

def save_data(df, path: str):
   df.to_csv(path, index=False)