import pandas as pd
from projeto_dados.metrics import calculate_metrics

def test_metrics_tables_shape():
    df_raw = pd.DataFrame({"id":[1,2], "idade":[20,30], "salario":[1000,2000]})
    df_clean = df_raw.copy()
    df_metrics = calculate_metrics(df_raw, df_clean)

    assert len(df_metrics) == 1
    assert set(["execution_date","rows_raw","rows_clean","rows_removed","percent_removed","nulls_raw","nulls_clean","avg_salary","median_age","std_salary","max_salary","min_salary","total_salary"]).issubset(df_metrics.columns)