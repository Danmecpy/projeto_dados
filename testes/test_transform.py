import pandas as pd
from projeto_dados.transform import clean_data

def test_clean_data_returns_df_and_dq():
    df = pd.DataFrame({
        "id": [1, 1, 2],
        "nome": [" A ", None, "Cliente_2"],
        "idade": [25, 200, 30],
        "salario": [5000, -10, 8000],
        "data_cadastro": ["2021-01-01", "1900-01-01", "2022-01-01"],
        "ativo": ["Sim", None, "Não"]
    })

    df_clean, dq = clean_data(df)

    assert isinstance(dq, dict)
    assert "rows_removed_total" in dq
    assert len(df_clean) >= 0
    assert df_clean["id"].is_unique
