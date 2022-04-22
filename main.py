#imports
import shelve
try:
    d = shelve.open('hipoints.txt')
    hipoints = d['hipoints']  # the score is read from disk
    d.close()
except:
    hipoints = 0

bullet1hit = False
bullet2hit = False
bullet3hit = False

import pygame
from pygame.locals import *
import random
from asteroid import Asteroid1
from asteroid2 import Asteroid2
from asteroid3 import Asteroid3
from ship import Ship
from title import Title
from bullet import Bullet
from doot import Dot
from sphere import Sphere
from shoe import Shoe
from settings import *

#initialize pygame
pygame.init()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
flags = DOUBLEBUF | HWSURFACE | SCALED | FULLSCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
font = pygame.font.Font("future.ttf", 80)

for dot in range(10):
    dot = Dot(random.randint(-4,4), random.randint(-1,1), random.randint(-1,1))
    dot.rect.x = random.randint(0,SCREEN_WIDTH)
    dot.rect.y = random.randint(0,SCREEN_HEIGHT)
    greengroup.add(dot)

#player
player = Ship()
player.rect.x = px
player.rect.y = py
playergroup.add(player)

#sat
sphere = Sphere(random.randint(-4,4), random.randint(-8,8), random.randint(-8,8))
sphere.rect.x = random.randint(0,SCREEN_WIDTH)
sphere.rect.y = random.randint(0,SCREEN_HEIGHT)
sgroup.add(sphere)

#shoe
shoe = Shoe(random.randint(-4,4), random.randint(-4,4), random.randint(-4,4))
shoe.rect.x = random.randint(0,SCREEN_WIDTH)
shoe.rect.y = random.randint(0,SCREEN_HEIGHT)
s2.add(shoe)

#bullets
bullet = Bullet()
bullet.rect.x = px + (player.rect.width/2)
bullet.rect.y = py + (player.rect.height/2)
bulletgroup.add(bullet)
notShot = True
bullet2 = Bullet()
bullet2.rect.x = px + (player.rect.width/2)
bullet2.rect.y = py + (player.rect.height/2)
bulletgroup.add(bullet2)
notShot2 = True
bullet3 = Bullet()
bullet3.rect.x = px + (player.rect.width/2)
bullet3.rect.y = py + (player.rect.height/2)
bulletgroup.add(bullet3)
notShot3 = True
bulletcount = 0

#title
title = Title()
title.rect.x = 660
title.rect.y = 200
titlegroup.add(title)

#asteroids
asteroid1 = Asteroid1()
asteroid1.rect.x = -80
asteroid1.rect.y = -80
agroup.add(asteroid1)
asteroid4 = Asteroid1()
asteroid4.rect.x = 480
asteroid4.rect.y = 280
agroup.add(asteroid4)
asteroid2 = Asteroid2()
asteroid2.rect.x = -80
asteroid2.rect.y = 880
agroup.add(asteroid2)
asteroid3 = Asteroid3()
asteroid3.rect.x = 1680
asteroid3.rect.y = 680
agroup.add(asteroid3)

#######################################################################################
while running:
#TITLE SCREEN
    if titley:
        count = count + 1
        screen.fill((0,0,0))
        textsurface = font.render('HI-SCORE: ' + str(hipoints), False, (255,255,255))
        textrect = textsurface.get_rect(topright = (SCREEN_WIDTH-10, 0))
        screen.blit(textsurface, textrect)
        textsurface2 = font.render('PRESS ENTER TO START', False, (255,255,255))
        textrect2 = textsurface2.get_rect(midbottom = (SCREEN_WIDTH/2, SCREEN_HEIGHT-200))
        if count < 60:    
            screen.blit(textsurface2, textrect2)
        if count > 70:
            count = 0
        titlegroup.draw(screen)
        titlegroup.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    titley = False
                    game = True
                    count = 0
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == QUIT:
                running = False
        pygame.display.update()
        clock.tick(60)       
#game over
    if bad:
        if points > hipoints:
            hipoints = points
            d = shelve.open('hipoints.txt')  # here you will save the score variable   
            d['hipoints'] = hipoints            # thats all, now it is saved on disk.
            d.close()
        px = SCREEN_WIDTH/2-25
        py = SCREEN_HEIGHT/2-25
        player.rect.x = px
        player.rect.y = py
        asteroid1.rect.x = -80
        asteroid1.rect.y = -80
        asteroid2.rect.x = 680
        asteroid2.rect.y = -80
        asteroid3.rect.x = -80
        asteroid3.rect.y = 680
        asteroid4.rect.x = 680
        asteroid4.rect.y = 680
        px = 300
        py = 400
        points = 0
        screen.fill((10,10,10))
        if ticker > 60:
            ticker = 0
        if ticker > 35 and ticker < 61:
            screen.blit(gameOverImg2, (SCREEN_WIDTH/2-gameOverImg2.get_width()/2, SCREEN_HEIGHT/2-gameOverImg2.get_height()/2))
        if ticker > 0  and ticker < 51:
            screen.blit(gameOverImg, (SCREEN_WIDTH/2-gameOverImg.get_width()/2, SCREEN_HEIGHT/2-gameOverImg.get_height()/2))

        ticker += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_RETURN:
                    ticker = 0
                    count = 0
                    atick = 0
                    hearts = 3
                    healthy = True
                    px = SCREEN_WIDTH/2-25
                    py = SCREEN_HEIGHT/2-25
                    player.rect.x = px
                    player.rect.y = py
                    asteroid1.rect.x = -80
                    asteroid1.rect.y = -80
                    asteroid4.rect.x = 480
                    asteroid4.rect.y = 280
                    asteroid2.rect.x = -80
                    asteroid2.rect.y = 880
                    asteroid3.rect.x = 1680
                    asteroid3.rect.y = 680
                    bad = False
                    titley = True

        pygame.display.update()
        clock.tick(60)
#Game loop start
    if game:
        dotcount += 1
        if dotcount < 2:

            for dot in greengroup:
                dot.rect.x = random.randint(0,SCREEN_WIDTH)
                dot.rect.y = random.randint(0,SCREEN_HEIGHT)
                dot.rot()
                
        else:
            dotcount = 3
        for dot in greengroup:
            if dot.x == 0:
                dot.x = 3
            if dot.y == 0:
                dot.y = 3
            if dot.rect.x < -50:
                dot.rect.x = SCREEN_WIDTH+50
            if dot.rect.x > SCREEN_WIDTH+50:
                dot.rect.x = -50
            if dot.rect.y < -50:
                dot.rect.y = SCREEN_HEIGHT+50
            if dot.rect.y > SCREEN_HEIGHT+50:
                dot.rect.y = -50
            dot.rot()



        if hearts == 0:

            bad = True
            game = False
        if chance == 0:
            chance = 3
        if chance3 == 0:
            chance3 = 3
        if chance5 == 0:
            chance5 = 3
        if chance7 == 0:
            chance7 = 3
        player.rect.x = px
        player.rect.y = py
#Carryover rect
        if shoe.rect.x > SCREEN_WIDTH+150:
            shoe.rect.x = -150
            shoe.x = random.randint(-4,4)
            shoe.y = random.randint(-4,4)
            shoe.angle = 3
        if shoe.rect.x < -150:
            shoe.rect.x = SCREEN_WIDTH+150
            shoe.x = random.randint(-4,4)
            shoe.y = random.randint(-4,4)
            shoe.angle = -2
        if shoe.rect.y > SCREEN_HEIGHT+150:
            shoe.rect.y = -150
            shoe.x = random.randint(-4,4)
            shoe.y = random.randint(-4,4)
            shoe.angle = 1
        if shoe.rect.y < -150:
            shoe.rect.y = SCREEN_HEIGHT+150
            shoe.x = random.randint(-4,4)
            shoe.y = random.randint(-4,4)
            shoe.angle = -4
        if sphere.rect.x > SCREEN_WIDTH+150:
            sphere.rect.x = -150
            sphere.x = random.randint(-4,4)
            sphere.y = random.randint(-4,4)
            sphere.angle = random.randint(-4,4)
        if sphere.rect.x < -150:
            sphere.rect.x = SCREEN_WIDTH+150
            sphere.x = random.randint(-4,4)
            sphere.y = random.randint(-4,4)
            sphere.angle = random.randint(-4,4)
        if sphere.rect.y > SCREEN_HEIGHT+150:
            sphere.rect.y = -150
            sphere.x = random.randint(-4,4)
            sphere.y = random.randint(-4,4)
            sphere.angle = random.randint(-4,4)
        if sphere.rect.y < -150:
            sphere.rect.y = SCREEN_HEIGHT+150
            sphere.x = random.randint(-4,4)
            sphere.y = random.randint(-4,4)
            sphere.angle = random.randint(-4,4)
        if asteroid1.rect.x > SCREEN_WIDTH+300:
            asteroid1.rect.x = -300
            chance = random.randint(-2,2)
            spinspeed = random.randint(-3,3)
            chance2 = random.randint(-2,2)
        elif asteroid1.rect.x < -300:
            asteroid1.rect.x = SCREEN_WIDTH+300
            chance = random.randint(-2,2)
            spinspeed = random.randint(-3,3)
            chance2 = random.randint(-2,2)
        elif asteroid1.rect.y > SCREEN_HEIGHT+300:
            asteroid1.rect.y = -300
            chance = random.randint(-2,2)
            spinspeed = random.randint(-3,3)
            chance2 = random.randint(-2,2)
        elif asteroid1.rect.y < -300:
            asteroid1.rect.y = SCREEN_HEIGHT+300
            chance = random.randint(-2,2)
            spinspeed = random.randint(-3,3)
            chance2 = random.randint(-2,2)
        elif asteroid2.rect.x > SCREEN_WIDTH+300:
            asteroid2.rect.x = -300
            chance3 = random.randint(-2,2)
            spinspeed2 = random.randint(-3,3)
            chance4 = random.randint(-2,2)
        elif asteroid2.rect.x < -300:
            asteroid2.rect.x = SCREEN_WIDTH+300
            chance3 = random.randint(-2,2)
            spinspeed2 = random.randint(-3,3)
            chance4 = random.randint(-2,2)
        elif asteroid2.rect.y > SCREEN_HEIGHT+300:
            asteroid2.rect.y = -300
            chance3 = random.randint(-2,2)
            spinspeed2 = random.randint(-3,3)
            chance4 = random.randint(-2,2)
        elif asteroid2.rect.y < -300:
            asteroid2.rect.y = SCREEN_HEIGHT+300
            chance3 = random.randint(-2,2)
            spinspeed2 = random.randint(-3,3)
            chance4 = random.randint(-2,2)
        elif asteroid3.rect.x > SCREEN_WIDTH+300:
            asteroid3.rect.x = -300
            chance5 = random.randint(-2,2)
            spinspeed3 = random.randint(-3,3)
            chance6 = random.randint(-2,4)
        elif asteroid3.rect.x < -300:
            asteroid3.rect.x = SCREEN_WIDTH+300
            chance5 = random.randint(-2,4)
            spinspeed3 = random.randint(-3,3)
            chance6 = random.randint(-2,2)
        elif asteroid3.rect.y > SCREEN_HEIGHT+300:
            asteroid3.rect.y = -300
            chance5 = random.randint(-2,2)
            spinspeed3 = random.randint(-3,3)
            chance6 = random.randint(-2,4)
        elif asteroid3.rect.y < -300:
            asteroid3.rect.y = SCREEN_HEIGHT+300
            chance5 = random.randint(-2,4)
            spinspeed3 = random.randint(-3,3)
            chance6 = random.randint(-2,2)
        elif asteroid4.rect.x > SCREEN_WIDTH+300:
            asteroid4.rect.x = -300
            chance7 = random.randint(-2,2)
            spinspeed4 = random.randint(-3,3)
            chance8 = random.randint(-2,2)
        elif asteroid4.rect.x < -300:
            asteroid4.rect.x = SCREEN_WIDTH+300
            chance7 = random.randint(-2,2)
            spinspeed4 = random.randint(-3,3)
            chance8 = random.randint(-2,2)
        elif asteroid4.rect.y > SCREEN_HEIGHT+300:
            asteroid4.rect.y = -300
            chance7 = random.randint(-2,2)
            spinspeed4 = random.randint(-3,3)
            chance8 = random.randint(-2,2)
        elif asteroid4.rect.y < -300:
            asteroid4.rect.y = SCREEN_HEIGHT+300
            chance7 = random.randint(-2,2)
            spinspeed4 = random.randint(-3,3)
            chance8 = random.randint(-2,2)
        else:
            pass
#Asteroid spin and angle
        asteroid1.change_angle = spinspeed
        asteroid1.rect.x += chance + offset
        asteroid1.rect.y += chance2 + offset
        asteroid2.change_angle = spinspeed2
        asteroid2.rect.x += chance3 + offset
        asteroid2.rect.y += chance4 + offset
        asteroid3.change_angle = spinspeed3
        asteroid3.rect.x += chance5 + offset
        asteroid3.rect.y += chance6 + offset
        asteroid4.change_angle = spinspeed4
        asteroid4.rect.x += chance7 + offset
        asteroid4.rect.y += chance8 + offset
#Player Carryover rect
        if px > SCREEN_WIDTH:
            px = 0
        if px < 0:
            px = SCREEN_WIDTH
        if py > SCREEN_HEIGHT-50:
            py = SCREEN_HEIGHT-50
        if py < 0:
            py = 0
#Keypress single time input
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_F12:
                    pygame.image.save(screen, "screenshot.png")
                if event.key == K_RETURN:
                    pass
            if event.type == KEYUP:
                if event.key == K_RETURN:
                    bulletcount = 0
#Keypress repeat input
        keys = pygame.key.get_pressed()
        player.still()
        if keys[K_w]:
            player.moveUp()
            py -= playerspeed
        if keys[K_w] and keys[K_a]:
            player.moveUpLeft()
            py -= (playerspeed/6)
            px -= (playerspeed/6)
        if keys[K_a]:
            player.moveLeft()
            px -= playerspeed
        if keys[K_a] and keys[K_s]:
            player.moveDownLeft()
            py += (playerspeed/6)
            px -= (playerspeed/6)
        if keys[K_s]:
            player.moveDown()
            py += playerspeed
        if keys[K_s] and keys[K_d]:
            player.moveDownRight()
            py += (playerspeed/6)
            px += (playerspeed/6)
        if keys[K_d]:
            player.moveRight()
            px += playerspeed
        if keys[K_d] and keys[K_w]:
            player.moveUpRight()
            py -= (playerspeed/6)
            px += (playerspeed/6)

            

        if keys[K_LSHIFT]:
            playerspeed = 12
        else:
            playerspeed = 8
        if keys[K_RETURN]:
            bulletcount += 1
            if bulletcount > 0 and bulletcount < 11:
                notShot = False
            if bulletcount > 5:
                notShot2 = False
            if bulletcount > 10:
                notShot3 = False
            if bulletcount > 40:
                bulletcount = 0

#Draw to the screen
        screen.fill((10, 10, 10))
        greengroup.draw(screen)
        agroup.draw(screen)
        sgroup.draw(screen)
        s2.draw(screen)
        bulletgroup.draw(screen)
        playergroup.draw(screen)
        
#Collision
        if pygame.sprite.collide_mask(asteroid1, player):

            if healthy == True:
                hearts = hearts - 1
                healthy = False
        if pygame.sprite.collide_mask(asteroid2, player):

            if healthy == True:
                hearts = hearts - 1
                healthy = False
        if pygame.sprite.collide_mask(asteroid3, player):

            if healthy == True:
                hearts = hearts - 1
                healthy = False
        if pygame.sprite.collide_mask(asteroid4, player):

            if healthy == True:
                hearts = hearts - 1
                healthy = False
        bullet_collision_list = pygame.sprite.spritecollide(bullet, agroup, False)
        bullet_collision_list2 = pygame.sprite.spritecollide(bullet2, agroup, False)
        bullet_collision_list3 = pygame.sprite.spritecollide(bullet3, agroup, False)
        green_collision_list = pygame.sprite.spritecollide(player, greengroup, False, pygame.sprite.collide_mask)
        for sprite in bullet_collision_list:
            points += 10
            offsetticker = offsetticker + 1
            bullet1hit = True
        for sprite in bullet_collision_list2:
            points += 10
            offsetticker = offsetticker + 1
            bullet2hit = True
        for sprite in bullet_collision_list3:
            points += 10
            offsetticker = offsetticker + 1
            bullet3hit = True
        if bullet1hit == True:
            bullet.rect.x -= random.randint(-4,4)
            bullet.rect.y -= random.randint(-4,4)
        if bullet2hit == True:
            bullet2.rect.x -= random.randint(-4,4)
            bullet2.rect.y -= random.randint(-4,4)
        if bullet3hit == True:
            bullet3.rect.x -= random.randint(-4,4)
            bullet3.rect.y -= random.randint(-4,4)
        for sprite in green_collision_list:
            if healthy == True:
                hearts = hearts - 1
                healthy = False
        if offsetticker > 30:
            offset = offset + .1
            offsetticker = 0
#    Rotation and updates/tick limit
        if healthy == False:
            atick = atick+1
            player.hurt()
        if atick > 120:
            healthy = True
            atick = 0
        
        for life in range(hearts):
            screen.blit(heart, (life*100,10))
        asteroid1.rot()
        asteroid2.rot()
        asteroid3.rot()
        asteroid4.rot()
        sphere.rot()
        shoe.rot()
        agroup.update()
#bullet shit        
        if notShot:
            bullet.rect.x = px + (player.rect.width/2)
            bullet.rect.y = py + (player.rect.height/2)
        if notShot == False:
            bullet.rect.y -= bulletspeed
        if bullet.rect.y < 0 or bullet.rect.y > screen.get_height() or bullet.rect.x < 0 or bullet.rect.x > screen.get_width():
            bullet1hit = False
            notShot = True

        if notShot2:
            bullet2.rect.x = px + (player.rect.width/2)
            bullet2.rect.y = py + (player.rect.height/2)
        if notShot2 == False:
            bullet2.rect.y -= bulletspeed
        if bullet2.rect.y < 0 or bullet2.rect.y > screen.get_height() or bullet2.rect.x < 0 or bullet2.rect.x > screen.get_width():
            notShot2 = True
            bullet2hit = False

        if notShot3:
            bullet3.rect.x = px + (player.rect.width/2)
            bullet3.rect.y = py + (player.rect.height/2)
        if notShot3 == False:
            bullet3.rect.y -= bulletspeed
        if bullet3.rect.y < 0 or bullet3.rect.y > screen.get_height() or bullet3.rect.x < 0 or bullet3.rect.x > screen.get_width():
            notShot3 = True
            bullet3hit = False
#final update cycle        
        sgroup.update()
        bulletgroup.update()
        playergroup.update()
        greengroup.update()
        s2.update()
        textsurface = font.render(str(points), False, (255,255,255))
        textrect = textsurface.get_rect(topright = (SCREEN_WIDTH-10, 0))
        screen.blit(textsurface, textrect)
        clock.tick(60)
        pygame.display.update()