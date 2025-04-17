import pandas as pd
import pyarrow.parquet as pq

df = pd.read_parquet('C:/Users/filip/OneDrive/academico/Dev/WebApp/eleicao22_fed_rio.parquet',
    columns=['SG_PARTIDO', 'NM_URNA_CANDIDATO', 'DS_CARGO', 'NM_BAIRRO', 'QT_VOTOS']
)

# Exibir as primeiras 5 linhas
df.head()