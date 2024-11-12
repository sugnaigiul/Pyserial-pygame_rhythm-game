import pygame

class Ship:
    def __init__(self):
        # Charge l'image de base du vaisseau
        self.original_image = pygame.image.load("./assets/ship.png")
        self.original_image = pygame.transform.scale(self.original_image, (50, 50))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(400, 570))
    
    def move(self, direction):
        if direction == "left" and self.rect.left >= 10:
            self.rect.move_ip(-10, 0)
        elif direction == "right" and self.rect.right <= 790:
            self.rect.move_ip(10, 0)
        
        # Met à jour l'inclinaison en fonction de la position du vaisseau
        self.update_tilt()

    def update_tilt(self):
        # Centre horizontal de l'écran
        screen_center_x = 400
        # Calcul de l'angle d'inclinaison en fonction de la distance par rapport au centre
        max_angle = 40  # Angle maximum d'inclinaison
        distance_from_center = self.rect.centerx - screen_center_x
        angle = -(distance_from_center / screen_center_x) * max_angle

        # Applique la rotation à l'image du vaisseau
        self.image = pygame.transform.rotate(self.original_image, -angle)
        # Met à jour le rectangle pour rester centré après la rotation
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


