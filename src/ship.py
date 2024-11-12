import pygame

# Classe Ship pour le vaisseau
class Ship:
    def __init__(self):
        self.image = pygame.image.load("./assets/ship.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(400, 570))
    
    def move(self, direction):
        if direction == "left" and self.rect.left >= 10:
            self.rect.move_ip(-10, 0)
        elif direction == "right" and self.rect.right <= 790:
            self.rect.move_ip(10, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

