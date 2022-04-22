import pygame
import random

#variables/flags
running = True
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920
px = SCREEN_WIDTH/2-25
py = SCREEN_HEIGHT/2-25
gameOverImg = pygame.image.load("gameover2.png")
gameOverImg2 = pygame.image.load("gameover3.png")
heart = pygame.image.load('heart.png').convert_alpha()
playerspeed = 8
pastpoints = 0
game = False
bad = False
ticker = 0
count = 0
collide = True
collide2 = True
collide3 = True
collide4 = True
atick = 0
atick2 = 0
atick3 = 0
atick4 = 0
hearts = 3
healthy = True
titley = True
bulletspeed = 40
bullets = 3
dotcount = 0
points = 0
offset = 0
offsetticker = 0
clock = pygame.time.Clock()
greengroup = pygame.sprite.Group()
playergroup = pygame.sprite.Group()
sgroup = pygame.sprite.Group()
s2 = pygame.sprite.Group()
bulletgroup = pygame.sprite.Group()
titlegroup = pygame.sprite.Group()
agroup = pygame.sprite.Group()
scorelist = []

#spins and randoms
asteroid1spinner = 0
chance = random.randint(1,4)
chance2 = random.randint(-4,4)
chance3 = random.randint(1,4)
chance4 = random.randint(-4,4)
chance5 = random.randint(1,4)
chance6 = random.randint(-4,4)
spinspeed = random.randint(-3,3)
spinspeed2 = random.randint(-3,3)
spinspeed3 = random.randint(-3,3)
chance7 = random.randint(1,4)
chance8 = random.randint(-4,4)
spinspeed4 = random.randint(-3,3)

