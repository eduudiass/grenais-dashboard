import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
import re

df = pd.read_csv("ultimos_25_grenais.csv")

st.title("🌟 Análise dos últimos 25 GreNais")

vitoria_counts = df["Vencedor"].value_counts()
vitoria_counts = vitoria_counts.reindex(["Internacional", "Grêmio", "Empate"], fill_value=0)

st.subheader(" Vitórias por Time")
st.bar_chart(vitoria_counts)

st.subheader(" Artilheiros nos últimos 25 GreNais")
gols_colunas = ["Gols (casa)", "Gols (visitante)"]
nomes_gols = []

for col in gols_colunas:
    for item in df[col].dropna():
        nomes = re.findall(r"([\w\sáéíúóãâôçêà]+) \(", item)
        nomes_gols.extend([nome.strip() for nome in nomes])

artilheiros = Counter(nomes_gols)
artilheiros_df = pd.DataFrame(artilheiros.items(), columns=["Jogador", "Gols"]).sort_values(by="Gols", ascending=False)
st.dataframe(artilheiros_df, hide_index=True)

st.subheader("📅 Tabela Completa")
st.dataframe(df)
