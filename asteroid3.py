import pygame

class Asteroid3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.og_surf = pygame.transform.smoothscale(pygame.image.load("asteroid3.png").convert_alpha(), (100, 100))
        self.surf = self.og_surf
        self.rect = self.surf.get_rect(center=(50, 50))
        
        self.angle = 0
        self.change_angle = 0
        self.image = self.surf
        self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    # THE MAIN ROTATE FUNCTION
    def rot(self):
        self.angle += self.change_angle
        self.surf = pygame.transform.rotate(self.og_surf, self.angle)
        
        self.angle = self.angle % 360
        self.rect = self.surf.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    # Move for keypresses
    def update(self):
        self.image = self.surf

    def redraw(self):
        self.rect.x = -80
        self.rect.y = -80