import random
import pygame
import math

# Classe Sphere pour les sphères ennemies
class Sphere:
    def __init__(self):
        self.radius = 20  # Rayon initial
        self.color = (255, 0, 0)
        self.x = random.randint(290, 510)  # Position x de départ 290/510
        self.y = -20  # Position y de départ
        self.growth_rate = 0.2  # Vitesse de croissance du rayon
        self.init_x = self.x # Position x de départ

    def move(self):
        self.y += 5  # Descend de 5 pixels par frame
        self.x = self.x + (self.init_x - 400) * 0.017 # Decalage pour effet de perspective
        self.radius += self.growth_rate  # Augmente le rayon de la sphère

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))  # Cast en entier pour x, y et le rayon

    def collides_with(self, ship):
        # Calcul de la distance entre le centre du vaisseau et celui de la sphère
        ship_center = ship.rect.center
        distance = math.sqrt((self.x - ship_center[0])**2 + (self.y - ship_center[1])**2)
        # Collision si la distance est inférieure à la somme des rayons
        return distance < self.radius + (ship.rect.width / 2)
