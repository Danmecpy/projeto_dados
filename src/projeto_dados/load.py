def save_data(df,path:str):
   df.to_csv(path, index=False)