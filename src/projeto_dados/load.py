from __future__ import annotations

from pathlib import Path
import pandas as pd


def save_data(df: pd.DataFrame, path: str | Path) -> None: 
    if df is None: 
        raise ValueError("save_data recebeu df=None (verifique o return do transform).")

    path = Path(path) # garantir que é Path
    path.parent.mkdir(parents=True, exist_ok=True) # garantir que pasta existe

    tmp = path.with_suffix(path.suffix + ".tmp") # arquivo temporário
    df.to_csv(tmp, index=False, encoding="utf-8") # escrever em arquivo temporário
    tmp.replace(path)  # escrita atômica (idempotente para o 'latest')

