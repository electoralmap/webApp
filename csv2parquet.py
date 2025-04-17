import pandas as pd

# df_data = pd.read_csv('data/eleicao22_fed_rio.csv', encoding='latin-1', sep=';')

# df_data.info()              # Informações de cada tipo de dado

# memory = df_data.memory_usage(deep=True) # Uso em bytes
# memory.sum()                # Soma de todos os Bytes de cada dado
# memory.sum() / (1024 ** 3)  # Uso de Gigabytes na memória

# memory / memory.sum() * 100 # Porcentagem de consumo de cada dado

# df_data["SG_PARTIDO"]

# df_data["SG_PARTIDO"].value_counts() # Descreve o somatório de valores

# #Convertendo os dados


# df_data["DS_CARGO"] = df_data["DS_CARGO"].astype("category")
# df_data["NR_CANDIDATO"] = pd.to_numeric(df_data["NR_CANDIDATO"], errors='coerce') 
# df_data["NM_CANDIDATO"] = df_data["NM_CANDIDATO"].astype("category")
# df_data["NM_URNA_CANDIDATO"] = df_data["NM_URNA_CANDIDATO"].astype("category")
# df_data["NR_PARTIDO"] = pd.to_numeric(df_data["NR_PARTIDO"], errors='coerce')
# df_data["SG_PARTIDO"] = df_data["SG_PARTIDO"].astype("category")
# df_data["NM_PARTIDO"] = df_data["NM_PARTIDO"].astype("category")
# df_data["NR_ZONA"] = pd.to_numeric(df_data["NR_ZONA"], errors='coerce')
# df_data["NR_SECAO"] = pd.to_numeric(df_data["NR_SECAO"], errors='coerce')
# df_data["NR_VOTAVEL"] = pd.to_numeric(df_data["NR_VOTAVEL"], errors='coerce')
# df_data["NM_VOTAVEL"] = df_data["NM_VOTAVEL"].astype("category")
# df_data["QT_VOTOS"] = pd.to_numeric(df_data["QT_VOTOS"], errors='coerce')
# df_data["ZONA_SECAO"] = pd.to_numeric(df_data["ZONA_SECAO"], errors='coerce')
# df_data["NM_MUNICIPIO"] = df_data["NM_MUNICIPIO"].astype("category")
# df_data["NM_LOCAL_VOTACAO"] = df_data["NM_LOCAL_VOTACAO"].astype("category")
# df_data["DS_ENDERECO"] = df_data["DS_ENDERECO"].astype("category")
# df_data["NM_BAIRRO"] = df_data["NM_BAIRRO"].astype("category")
# df_data["NR_LATITUDE"] = pd.to_numeric(df_data["NR_LATITUDE"], errors='coerce')
# df_data["NR_LONGITUDE"] = pd.to_numeric(df_data["NR_LONGITUDE"], errors='coerce')
# df_data["NR_CEP"] = pd.to_numeric(df_data["NR_CEP"], errors='coerce')

# df_data.info()

# #$$
# #pyarrow

# df_data.to_parquet("eleicao22_fed_rio.parquet")
# df_data2 = pd.read_parquet("eleicao22_fed_rio.parquet")

# df_data2.info()

import streamlit as st
import pandas as pd

import pyarrow as pa
import pyarrow.parquet as pq

import folium as fl
from streamlit_folium import st_folium

# Display do Mapa



