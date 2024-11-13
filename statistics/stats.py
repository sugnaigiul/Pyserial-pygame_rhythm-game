import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données depuis le fichier CSV
df = pd.read_csv('./../src/player_data.csv', header=None, names=['Player', 'Score', 'Games'])

# Trie des données par Score pour 1er graphique
df_sorted = df.sort_values(by='Score')

# Deux sous-graphiques côte à côte
plt.figure(figsize=(16, 6))

# Premier graphique : Barres triées par score
plt.subplot(1, 2, 1)  # 1 ligne, 2 colonnes, 1er graphique
plt.bar(df_sorted['Player'], df_sorted['Score'], color='skyblue')
plt.xlabel('Joueurs')
plt.ylabel('Score')
plt.title('Scores des joueurs triés en ordre croissant')
plt.xticks(rotation=90)

# Deuxième graphique : Scatter plot (Score vs Games)
plt.subplot(1, 2, 2)  # 1 ligne, 2 colonnes, 2ème graphique
plt.scatter(df['Games'], df['Score'], color='coral')
plt.xlabel('Nombre de parties')
plt.ylabel('Score')
plt.title('Score en fonction du nombre de parties')
plt.grid(True)

# Ajuster l'espacement entre les graphiques
plt.tight_layout()
plt.show()
