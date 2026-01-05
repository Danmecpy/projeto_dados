import pandas as pd
from datetime import datetime

def calculate_metrics(
    df_raw: pd.DataFrame,
    df_clean: pd.DataFrame
) -> pd.DataFrame:
    """
    Calcula métricas de qualidade do pipeline e métricas básicas de negócio.
    Retorna um DataFrame (1 linha) pronto para Power BI.
    """

    metrics = {
        # =========================
        # METADADOS
        # =========================
        "execution_date": datetime.now(),

        # =========================
        # VOLUME
        # =========================
        "rows_raw": len(df_raw),
        "rows_clean": len(df_clean),
        "rows_removed": len(df_raw) - len(df_clean),
        "percent_removed": round(
            (len(df_raw) - len(df_clean)) / len(df_raw) * 100, 2
        ),

        # =========================
        # QUALIDADE (ANTES)
        # =========================
        "nulls_raw": int(df_raw.isna().sum().sum()),

        # =========================
        # QUALIDADE (DEPOIS)
        # =========================
        "nulls_clean": int(df_clean.isna().sum().sum()),

        # =========================
        # MÉTRICAS DE NEGÓCIO (LIMPO)
        # =========================
        "avg_salary": round(df_clean["salario"].mean(), 2),
        "median_age": int(df_clean["idade"].median()),
        "std_salary": round(df_clean["salario"].std(), 2),
        "max_salary": df_clean["salario"].max(),
        "min_salary": df_clean["salario"].min(),
        "total_salary": round(df_clean["salario"].sum(), 2),
    }

    return pd.DataFrame([metrics])
