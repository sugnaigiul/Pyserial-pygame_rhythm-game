import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
df = pd.read_csv('./../src/player_data.csv', header=None, names=['Player', 'Score', 'Games'])

# Trier les données par Score pour le premier graphique
df_sorted = df.sort_values(by='Score')

# Compter le nombre de joueurs avec une seule partie et avec plusieurs parties
one_game_count = len(df[df['Games'] == 1])
multiple_games_count = len(df[df['Games'] > 1])

# Créer une figure avec trois sous-graphiques
plt.figure(figsize=(18, 6))

# Premier graphique : Barres triées par score
plt.subplot(1, 3, 1)  # 1 ligne, 3 colonnes, 1er graphique
plt.bar(df_sorted['Player'], df_sorted['Score'], color='skyblue')
plt.xlabel('Joueurs')
plt.ylabel('Highscore')
plt.title('Highscores des joueurs triés en ordre croissant')
plt.xticks(rotation=90)

# Deuxième graphique : Scatter plot (Score vs Games)
plt.subplot(1, 3, 2)  # 1 ligne, 3 colonnes, 2ème graphique
plt.scatter(df['Games'], df['Score'], color='coral')
plt.xlabel('Nombre de parties')
plt.ylabel('Highscore')
plt.title('Highscore en fonction du nombre de parties')
plt.grid(True)

# Troisième graphique : Diagramme en camembert (proportion de joueurs)
plt.subplot(1, 3, 3)  # 1 ligne, 3 colonnes, 3ème graphique
plt.pie(
    [one_game_count, multiple_games_count],
    labels=['1 partie', 'Plusieurs parties'],
    autopct='%1.1f%%',
    startangle=140,
    colors=['lightgreen', 'lightskyblue']
)
plt.title('Proportion de joueurs par nombre de parties')

# Ajuster l'espacement entre les graphiques
plt.tight_layout()
plt.show()
