import pygame

class Dot(pygame.sprite.Sprite):
    def __init__(self, angle, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.og_surf = pygame.transform.smoothscale(pygame.image.load("greendot.png").convert_alpha(), (20, 20))
        self.surf = self.og_surf
        self.rect = self.surf.get_rect(center=(10,10))
        self.x = x
        self.y = y
        self.angle = 0
        self.change_angle = angle
        self.image = self.surf
        self.image.get_rect(center=self.rect.center)

    # THE MAIN ROTATE FUNCTION
    def rot(self):
        self.angle += self.change_angle
        self.surf = pygame.transform.rotate(self.og_surf, self.angle)
        
        self.angle = self.angle % 360
        self.rect = self.surf.get_rect(center=self.rect.center)

    # Move for keypresses
    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y
        self.image = self.surf
        if self.x == 0:
            self.x == 1
        if self.y == 0:
            self.y == 1
    
    def redraw(self):
        self.rect.x = -80
        self.rect.y = -80