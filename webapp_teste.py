import streamlit as st
import pandas as pd
import pyarrow.parquet as pq
import folium as fl
from streamlit_folium import folium_static
from folium.features import GeoJsonTooltip
import os

# Configuração da página
st.set_page_config(
    page_title="Mapa Eleitoral",
    page_icon="🧊",
    layout="wide",
)

# Carregar dados
df = pd.read_parquet(
    'C:/Users/filip/OneDrive/academico/Dev/WebApp/eleicao22_fed_rio.parquet',
    columns=['SG_PARTIDO', 'NM_URNA_CANDIDATO', 'DS_CARGO', 'NM_BAIRRO', 'QT_VOTOS']
)

# Verificação de caminho do GeoJSON
geojson_path = os.path.join( "Limite_Bairro.geojson")
if not os.path.exists(geojson_path):
    st.error(f"Arquivo GeoJSON não encontrado: {geojson_path}")
    st.stop()

# Barra lateral - Seleção de Partido
partidos = df["SG_PARTIDO"].value_counts().index
box_part = st.sidebar.selectbox("Partido", partidos)

# Filtrar dados com base no partido selecionado
sel_part = df[df["SG_PARTIDO"] == box_part]

# Verificar se sel_part tem dados
if sel_part.empty:
    st.sidebar.warning("Nenhum candidato encontrado para o partido selecionado.")
    st.stop()

# Barra lateral - Seleção de Candidato
candidatos = sel_part["NM_URNA_CANDIDATO"].value_counts().index
box_cand = st.sidebar.selectbox("Candidato", candidatos)

# Filtrar dados com base no candidato selecionado
cand_data = sel_part[sel_part["NM_URNA_CANDIDATO"] == box_cand]

# Verificar se cand_data tem dados
if cand_data.empty:
    st.warning("Nenhum dado disponível para o candidato selecionado.")
    st.stop()

# Calcular a soma dos votos para o candidato selecionado
votos = cand_data['QT_VOTOS'].sum()
votos = int(votos)  # Converter para inteiro

# Informações do candidato
cand_stats = cand_data.iloc[0]

# Exibir informações do candidato
st.title(f"{cand_stats['NM_URNA_CANDIDATO']}")
st.markdown(f"Candidato ao **cargo** de **{cand_stats['DS_CARGO']}**")
st.markdown(f"Votação Total: {votos:,.0f}".replace(',', '.'))

# Inicializar o mapa com uma localização central
mapa = fl.Map(location=[-22.928777, -43.423878], zoom_start=10, tiles='CartoDB positron')

# Adicionar Choropleth ao mapa (somente se cand_data não estiver vazio)
if not cand_data.empty:
    choropleth = fl.Choropleth(
        geo_data=geojson_path,
        data=cand_data,
        columns=["NM_BAIRRO", "QT_VOTOS"],
        key_on="feature.properties.NOME",
        fill_color='YlGn',
        nan_fill_color='white',
        line_opacity=0.7,
        fill_opacity=0.7,
        highlight=True,
        legend_name='Total de Votos'
    )
    choropleth.add_to(mapa)
else:
    st.warning("Não há dados de votos para exibir no mapa.")

# Adicionar tooltip
fl.GeoJson(
    data=geojson_path,
    style_function=lambda feature: {
        'fillColor': 'yellow',
        'color': 'black',
        'weight': 0.5,
        'fillOpacity': 0.1,
    },
    tooltip=fl.GeoJsonTooltip(
        fields=['NOME'],
        aliases=['Bairro: '],
        localize=True,
        sticky=False,
    )
).add_to(mapa)

# Exibir o mapa usando folium_static
folium_static(mapa)

#st.write("sel_part shape:", sel_part.shape)
#st.write("cand_data shape:", cand_data.shape)
#st.write("Candidatos disponíveis:", sel_part["NM_URNA_CANDIDATO"].unique())
#st.write("eleicao22_fed_rio.columns", df.columns)
