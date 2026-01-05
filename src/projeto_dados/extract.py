from __future__ import annotations

from pathlib import Path
import pandas as pd


def extract_data(path: str | Path) -> pd.DataFrame:
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    # encoding="utf-8-sig" ajuda quando CSV vem com BOM (muito comum no Windows/Excel)
    df = pd.read_csv(path, encoding="utf-8-sig")

    return df
