import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# =========================
# CONFIGURAÇÕES
# =========================
np.random.seed(42)
N_RECORDS = 1000
OUTPUT_PATH = "data/raw/dados_brutos_sujos.csv"

os.makedirs("data/raw", exist_ok=True)

# =========================
# GERAR DADOS BASE
# =========================
df = pd.DataFrame({
    "id": np.arange(1, N_RECORDS + 1),
    "nome": [f"Cliente_{i}" for i in range(1, N_RECORDS + 1)],
    "idade": np.random.randint(18, 80, N_RECORDS),
    "salario": np.random.uniform(1000, 10000, N_RECORDS).round(2),
    "data_cadastro": pd.date_range("2020-01-01", periods=N_RECORDS, freq="D"),
    "ativo": np.random.choice([True, False], N_RECORDS)
})

# =========================
# INJETAR FALHAS
# =========================

# 1️⃣ Idades inválidas
df.loc[np.random.choice(df.index, 20), "idade"] = np.random.choice([-5, 0, 150, None], 20)

# 2️⃣ Salários inválidos
df.loc[np.random.choice(df.index, 20), "salario"] = np.random.choice(
    [-1000, 0, 999999, "erro"], 20
)

# 3️⃣ Datas inválidas
df.loc[np.random.choice(df.index, 15), "data_cadastro"] = np.random.choice(
    ["2025-13-01", "1900-01-01", None], 15
)

# 4️⃣ Nomes inválidos
df.loc[np.random.choice(df.index, 25), "nome"] = np.random.choice(
    ["", "   ", None, "N/A"], 25
)

# 5️⃣ Duplicar IDs
duplicate_ids = np.random.choice(df["id"], 10)
df.loc[np.random.choice(df.index, 10), "id"] = duplicate_ids

# 6️⃣ Ativo inconsistente
df.loc[np.random.choice(df.index, 20), "ativo"] = np.random.choice(
    ["Sim", "Não", "TRUE", "FALSE", None], 20
)

# =========================
# SALVAR
# =========================
df.to_csv(OUTPUT_PATH, index=False)

print("⚠️ Dados SUJOS gerados com sucesso!")
print(f"📁 Arquivo: {OUTPUT_PATH}")
print(f"📊 Total de registros: {len(df)}")
