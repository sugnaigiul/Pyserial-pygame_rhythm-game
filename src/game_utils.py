import pygame
import csv
from pygame.locals import *

# Création des rectangles inclinés pour former une route
# Rectangle gauche
left_rect = pygame.Surface((800, 20), pygame.SRCALPHA)  # Utilise un Surface avec transparence
left_rect.fill((255, 255, 255))
left_rect = pygame.transform.rotate(left_rect, 65)  # Inclinée de 30 degrés
left_rect_rect = left_rect.get_rect(center=(100, 300))  # Place le rectangle en centre gauche

# Rectangle droit
right_rect = pygame.Surface((800, 20), pygame.SRCALPHA)
right_rect.fill((255, 255, 255))
right_rect = pygame.transform.rotate(right_rect, -65)  # Inclinée de -30 degrés
right_rect_rect = right_rect.get_rect(center=(700, 300))  # Place le rectangle en centre droit

# Fonction pour lire et trier les données du leaderboard
def show_leaderboard(screen):
    font = pygame.font.Font("assets/fonts/F25_Bank_Printer.ttf", 25)
    screen.fill((0, 0, 0))
    screen.blit(left_rect, left_rect_rect)
    screen.blit(right_rect, right_rect_rect)

    # Lire et trier les données par high score de manière décroissante
    try:
        with open("player_data.csv", newline="") as csvfile:
            reader = csv.reader(csvfile)
            player_data = sorted(reader, key=lambda row: int(row[1]), reverse=True)
    except FileNotFoundError:
        player_data = []  # Si le fichier n'existe pas

    # Affichage du leaderboard
    title_text = font.render("Leaderboard", True, (255, 255, 255))
    screen.blit(title_text, (300, 200))
    
    for i, (name, score, games) in enumerate(player_data[:5], start=1):  # Affiche les 5 meilleurs scores
        player_text = font.render(f"{i}. {name} - Score: {score} - Games: {games}", True, (255, 255, 255))
        screen.blit(player_text, (130, 300 + i * 40))

    pygame.display.flip()

    # Attendre une touche pour quitter le leaderboard
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

# Fonction pour obtenir les initiales du joueur
def get_player_initials(screen):
    initials = ""
    font = pygame.font.Font("assets/fonts/F25_Bank_Printer.ttf", 30)
    input_active = True

    while input_active:
        screen.fill((0, 0, 0))
        screen.blit(left_rect, left_rect_rect)
        screen.blit(right_rect, right_rect_rect)
        
        prompt_text = font.render("Enter your 3 initials:", True, (255, 255, 255))
        screen.blit(prompt_text, (165, 250))
        initials_text = font.render(initials, True, (255, 255, 255))
        screen.blit(initials_text, (368, 300))

        leaderboard_text = font.render("Press ESC for leaderboard", True, (255, 255, 255))
        screen.blit(leaderboard_text, (150, 500))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_leaderboard(screen)  # Affiche le leaderboard si Échap est pressé
                elif event.key == pygame.K_RETURN and len(initials) == 3:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE and len(initials) > 0:
                    initials = initials[:-1]
                elif event.unicode.isalpha() and len(initials) < 3:
                    initials += event.unicode.upper()

    return initials

# Fonction pour relancer une partie
def replay(screen, score):
    font = pygame.font.Font("assets/fonts/F25_Bank_Printer.ttf", 25)
    input_active = True

    while input_active:
        screen.fill((0, 0, 0))
        # On dessine les rectangles inclinés
        screen.blit(left_rect, left_rect_rect)
        screen.blit(right_rect, right_rect_rect)
        # Affichage du texte "Score"
        label_text = font.render("Final Score :", True, (255, 255, 255))
        screen.blit(label_text, (290, 60))
        # Affichage de la valeur de score
        score_text = font.render(str(score), True, (255, 255, 255))
        screen.blit(score_text, (290, 100))
        prompt_text = font.render("Start again ? (y/n)", True, (255, 255, 255))
        screen.blit(prompt_text, (250, 400))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False