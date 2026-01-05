# Importar bibliotecas necessárias
import os
import pandas as pd
import numpy as np

# Criar diretório 'data/raw' se não existir
os.makedirs('data/raw', exist_ok=True)

# Gerar dados brutos com seed para reprodutibilidade
np.random.seed(42)
# Definir quantidade de registros a gerar
n_records = 1000

# Criar dicionário com dados para o DataFrame
data = {
   'id': range(1, n_records + 1),  # IDs de 1 a 1000
   'nome': [f'Cliente_{i}' for i in range(1, n_records + 1)],  # Nomes cliente
   'idade': np.random.randint(18, 80, n_records),  # Idades aleatórias entre 18 e 80
   'salario': np.random.uniform(1000, 10000, n_records),  # Salários aleatórios entre 1000 e 10000
   'data_cadastro': pd.date_range('2020-01-01', periods=n_records, freq='D'),  # Datas sequenciais a partir de 2020-01-01
   'ativo': np.random.choice([True, False], n_records)  # Status ativo/inativo aleatório
}

# Converter dicionário em DataFrame
df = pd.DataFrame(data)

# Salvar DataFrame em arquivo CSV sem índice de linha
df.to_csv('data/raw/dados_brutos.csv', index=False)

# Exibir mensagem de sucesso com quantidade de registros
print(f"✓ Dados brutos criados: {n_records} registros")
# Exibir caminho do arquivo salvo
print(f"✓ Arquivo salvo em: data/raw/dados_brutos.csv")