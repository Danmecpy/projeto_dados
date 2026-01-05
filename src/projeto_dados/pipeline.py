from projeto_dados.extract import extract_data
from projeto_dados.transform import clean_data
from projeto_dados.load import save_data

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

extract_path = BASE_DIR / "data" / "raw" / "dados_brutos.csv"
load_path = BASE_DIR / "data" / "processed" / "data_limpos.csv"

def run_pipeline(extract_path: str, load_path: str):
    # Extract
    df = extract_data(extract_path)
    
    # Transform
    df_cleaned = clean_data(df)
    
    # Load
    save_data(df_cleaned, load_path)
    
run_pipeline(extract_path, load_path)
    