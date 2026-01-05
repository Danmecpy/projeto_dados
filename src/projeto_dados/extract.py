import pandas as pd


def extract_data(df,path: str):
    return pd.read_csv(path)