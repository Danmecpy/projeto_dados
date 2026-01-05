from __future__ import annotations

from pathlib import Path
import pandas as pd


def save_data(df: pd.DataFrame, path: str | Path) -> None:
    if df is None:
        raise ValueError("save_data recebeu df=None (verifique o return do transform).")

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    # tmp no mesmo diretório (idempotência + evita arquivo corrompido)
    tmp = path.with_name(f"{path.stem}.tmp{path.suffix}")

    suffix = path.suffix.lower()

    if suffix == ".csv":
        df.to_csv(tmp, index=False, encoding="utf-8")
    elif suffix in (".parquet", ".pq"):
        df.to_parquet(tmp, index=False, engine="pyarrow")
    else:
        raise ValueError(f"Formato não suportado: {suffix}. Use .csv ou .parquet")

    tmp.replace(path)  # troca atômica
