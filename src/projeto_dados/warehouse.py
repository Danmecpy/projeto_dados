from __future__ import annotations
from pathlib import Path
import duckdb


def get_conn(db_path: str | Path) -> duckdb.DuckDBPyConnection:
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(str(db_path))


def _reader_expr(path: Path) -> str:
    # DuckDB prefere paths com /
    p = path.resolve().as_posix()
    suf = path.suffix.lower()

    if suf == ".csv":
        return f"read_csv_auto('{p}')"
    if suf in (".parquet", ".pq"):
        return f"read_parquet('{p}')"

    raise ValueError(f"Formato não suportado: {suf}. Use .csv ou .parquet")


def load_file_as_table(conn: duckdb.DuckDBPyConnection, file_path: str | Path, table: str) -> None:
    file_path = Path(file_path)
    expr = _reader_expr(file_path)
    conn.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM {expr}")


def init_schema(conn: duckdb.DuckDBPyConnection) -> None:
    # opcional: um schema para organizar
    conn.execute("CREATE SCHEMA IF NOT EXISTS lake;")
