from pathlib import Path
import pandas as pd

from projeto_dados.pipeline import run_pipeline

def test_pipeline_runs_and_outputs(tmp_path: Path):
    # cria entrada fake
    raw_dir = tmp_path / "data" / "raw"
    processed_dir = tmp_path / "data" / "processed"
    raw_dir.mkdir(parents=True)
    processed_dir.mkdir(parents=True)

    input_csv = raw_dir / "dados_brutos.csv"
    output_clean = processed_dir / "dados_limpos.csv"

    df = pd.DataFrame({
        "id": [1, 2],
        "nome": ["Cliente_1", "Cliente_2"],
        "idade": [25, 30],
        "salario": [5000, 8000],
        "data_cadastro": ["2021-01-01", "2022-01-01"],
        "ativo": ["true", "true"],
    })
    df.to_csv(input_csv, index=False)

    # roda pipeline com paths temporários
    run_pipeline(input_csv, output_clean)

    assert output_clean.exists()
    df_out = pd.read_csv(output_clean)
    assert len(df_out) > 0
