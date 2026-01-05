from pathlib import Path
import logging
from datetime import datetime

from projeto_dados.extract import extract_data
from projeto_dados.transform import clean_data
from projeto_dados.load import save_data
from projeto_dados.metrics import calculate_metrics

# =========================
# PATHS
# =========================
BASE_DIR = Path(__file__).resolve().parents[2]

extract_path = BASE_DIR / "data" / "raw" / "dados_brutos.csv"
load_clean_path = BASE_DIR / "data" / "processed" / "dados_limpos.parquet"
load_metrics_path = BASE_DIR / "data" / "processed" / "metrics.parquet"


# =========================
# LOGS (pequeno, corporativo)
# =========================
def setup_logger() -> logging.Logger:
    logs_dir = BASE_DIR / "logs"
    logs_dir.mkdir(exist_ok=True)

    logger = logging.getLogger("pipeline")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    fh = logging.FileHandler(logs_dir / "pipeline.log", encoding="utf-8")
    fh.setFormatter(fmt)

    sh = logging.StreamHandler()
    sh.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger

# =========================
# PIPELINE
# =========================
def run_pipeline(extract_path: Path, load_clean_path: Path):
    logger = setup_logger()
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    logger.info(f"RUN {run_id} | start")

    # Extract
    df_raw = extract_data(extract_path)
    logger.info(f"RUN {run_id} | extracted rows={len(df_raw)}")

    # Transform (AGORA retorna df + dq)
    df_cleaned, dq = clean_data(df_raw)
    logger.info(
        f"RUN {run_id} | cleaned rows={len(df_cleaned)} removed={dq.get('rows_removed_total')}"
    )

    # Metrics (ANTES DO LOAD)
    df_metrics = calculate_metrics(df_raw, df_cleaned)

    # Se calculate_metrics retornar dict por algum motivo, converte:
    try:
        import pandas as pd
        if isinstance(df_metrics, dict):
            df_metrics = pd.DataFrame([df_metrics])
    except Exception:
        pass

    # =========================
    # SLA leve + alertas (apenas log)
    # =========================
    # exemplo: se remover mais que 20%, alerta
    removed = dq.get("rows_removed_total", 0)
    percent_removed = (removed / len(df_raw) * 100) if len(df_raw) else 0.0

    if percent_removed > 60:
        logger.warning(f"RUN {run_id} | SLA_VIOLATION | percent_removed={percent_removed:.2f}% > 60%")

    # Anexa run_id (útil no Power BI)
    if hasattr(df_metrics, "insert"):
        df_metrics.insert(0, "run_id", run_id)

    # Load (idempotente via escrita atômica)
    save_data(df_cleaned, load_clean_path)
    save_data(df_metrics, load_metrics_path)

    logger.info(f"RUN {run_id} | done")

# =========================
# ENTRYPOINT
# =========================
if __name__ == "__main__":
    run_pipeline(extract_path, load_clean_path)
    print("✅ Pipeline executada com sucesso!")
