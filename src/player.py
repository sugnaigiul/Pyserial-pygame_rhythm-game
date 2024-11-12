import csv

# Classe Player pour gérer les informations du joueur
class Player:
    def __init__(self, name):
        self.name = name
        self.high_score = 0
        self.num_games = 0

    def save_data(self):
        # Chemin vers le fichier CSV
        file_name = "player_data.csv"

        # Lire les données existantes dans le CSV
        players_data = []
        player_exists = False
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.name:
                    player_exists = True
                    # Mettre à jour les informations du joueur
                    row[1] = str(max(self.high_score, int(row[1])))  # Mettre à jour le high score si nécessaire
                    row[2] = str(int(row[2]) + 1)  # Incrémenter le nombre de parties
                players_data.append(row)

        # Si le joueur n'existe pas, ajouter une nouvelle ligne
        if not player_exists:
            players_data.append([self.name, str(self.high_score), str(self.num_games)])

        # Réécrire les données dans le CSV
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(players_data)

    def load_data(self):
        # Charger les données du joueur depuis le CSV
        file_name = "player_data.csv"
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.name:
                    self.high_score = int(row[1])
                    self.num_games = int(row[2])

    def update_score(self, new_score):
        self.score = new_score
        self.high_score = max(self.high_score, new_score)
