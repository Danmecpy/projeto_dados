from pathlib import Path
from projeto_dados.warehouse import get_conn, init_schema, load_file_as_table

BASE_DIR = Path(__file__).resolve().parents[2] # projeto_dados /src/projeto_dados/warehouse.py
DB_PATH = BASE_DIR / "data" / "warehouse" / "warehouse.duckdb"

# ajuste extensão conforme você estiver usando (.csv ou .parquet)
CLEAN_PATH = BASE_DIR / "data" / "processed" / "dados_limpos.parquet"
METRICS_PATH = BASE_DIR / "data" / "processed" / "metrics.parquet"

def main():
    conn = get_conn(DB_PATH)
    init_schema(conn)

    load_file_as_table(conn, CLEAN_PATH, "lake.dados_limpos")
    load_file_as_table(conn, METRICS_PATH, "lake.metrics")

    # sanity check
    print(conn.execute("SELECT COUNT(*) AS n FROM lake.dados_limpos").fetchdf())
    print(conn.execute("SELECT * FROM lake.metrics").fetchdf())

    conn.close()
    print(f"✅ DuckDB criado/atualizado em: {DB_PATH}")

if __name__ == "__main__":
    main()
