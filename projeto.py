import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

try:
    df = pd.read_csv("ultimos_25_grenais.csv")
except FileNotFoundError:
    print(" Arquivo 'ultimos_25_grenais.csv' não encontrado.")
    exit()

vits = df["Vencedor"].value_counts()
vits = vits.rename({"Internacional": "Inter", "Grêmio": "Grêmio", "Empate": "Empate"})

print("\n📊 Vitórias:")
print(vits)

plt.figure(figsize=(6, 4))
vits.plot(kind='bar', color=["red", "blue", "gray"])
plt.title("Vitórias nos últimos 25 GreNais")
plt.ylabel("Quantidade")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

df["Gols (casa)"] = df["Gols (casa)"].fillna('')
df["Gols (visitante)"] = df["Gols (visitante)"].fillna('')

total_gols_inter = 0
total_gols_gremio = 0

for _, row in df.iterrows():
    gols_casa = len([g for g in row["Gols (casa)"].split(",") if g.strip()])
    gols_visitante = len([g for g in row["Gols (visitante)"].split(",") if g.strip()])
    if "Internacional" in row["Placar"]:
        total_gols_inter += gols_casa
        total_gols_gremio += gols_visitante
    else:
        total_gols_inter += gols_visitante
        total_gols_gremio += gols_casa

print("\n Total de Gols:")
print(f"Internacional: {total_gols_inter}")
print(f"Grêmio: {total_gols_gremio}")

plt.figure(figsize=(6, 4))
plt.bar(["Inter", "Grêmio"], [total_gols_inter, total_gols_gremio], color=["red", "blue"])
plt.title("Total de Gols nos últimos 25 GreNais")
plt.ylabel("Gols Marcados")
plt.tight_layout()
plt.show()

gols_series = df['Gols (casa)'] + ',' + df['Gols (visitante)']
todos_gols = []

for linha in gols_series:
    artilheiros = [re.sub(r'\s*\(.*?\)', '', nome).strip() for nome in linha.split(',') if nome.strip()]
    todos_gols.extend(artilheiros)

contagem_artilheiros = Counter(todos_gols)
df_artilheiros = pd.DataFrame(contagem_artilheiros.items(), columns=["Jogador", "Gols"])
df_artilheiros = df_artilheiros.sort_values(by="Gols", ascending=False)

print("\n Artilheiros dos últimos 25 GreNais:\n")
print(df_artilheiros.to_string(index=False))
plt.figure(figsize=(10, 6))
plt.bar(df_artilheiros["Jogador"], df_artilheiros["Gols"], color="purple")
plt.xticks(rotation=45, ha='right')
plt.title("Artilheiros dos últimos 25 GreNais")
plt.xlabel("Jogador")
plt.ylabel("Gols")
plt.tight_layout()
plt.show()
