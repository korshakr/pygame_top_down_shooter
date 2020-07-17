import conf
from player import Player
from wall import Block
from scope import Scope
from bullet import Bullet
import enemy

from pygame.math import Vector2

import math


def draw_map(display,fps):
    world = conf.pygame.Surface((conf.SURFACEWIDTH,conf.SURFACEHIGHT))
    
    mainClock = conf.pygame.time.Clock()

    player = Player()
    bullets = []
    
    
   # scope = Scope()

    enemies = [enemy.monster_lvl0()]


    camera_pos = (conf.X_CAMERA,conf.Y_CAMERA)

    blocks = createBlocks(world)
   

    angle = 0
    while True:
        for event in conf.pygame.event.get():
            if event.type == conf.pygame.QUIT:
                return

            if event.type == conf.pygame.MOUSEBUTTONDOWN and event.button == 1:
                bullets.append(Bullet(player.player_rect.center,angle))

            # if conf.pygame.mouse.get_pressed()[0]:
            #     bullets.append(Bullet(player.player_rect.center,angle))
                
                
        camera_pos = player.move(camera_pos,blocks)

        current_position_cursor = (conf.pygame.mouse.get_pos()[0] - camera_pos[0], conf.pygame.mouse.get_pos()[1] - camera_pos[1])
        x,y = Vector2(current_position_cursor) - player.player_rect.center
        angle = math.degrees(math.atan2(y,x))

        

        if player.isLive:
            isDead(player,enemies)
            

        display.fill(conf.COLORS['BLACK'])
        world.fill(conf.COLORS['WHITE'])

        for block in blocks:
            block.render(world)
       
        if player.isLive:
            player.render(world)

        draw_enemies(world,player,enemies,blocks)

        draw_bullets(world,bullets,blocks,enemies)
                
        display.blit(world,camera_pos)

        conf.pygame.display.update()

        mainClock.tick(fps)



def isDead(player,enemies):
    for enemy in enemies:
        if player.player_rect.colliderect(enemy.monster_lvl0_rect):
            player.isLive = False
            break


def createBlocks(world):
    blocks = []
    for x in range(0,800,5):
        blocks.append(Block(x,0))
        

    for y in range(0,801,5):
        for x in [0,800]:
            blocks.append(Block(x,y))
            
    
    for x in range(0,800,5):
        if x in range(530,600):
            continue
        blocks.append(Block(x,800))

    return blocks
        

def draw_enemies(display,player,enemies,blocks):
    if enemies:
        for enemy in enemies[:]:
            if enemy.health > 0: 
                enemy.render(display,player,blocks)
            else:
                enemies.remove(enemy)


def draw_bullets(display,bullets,blocks,enemies):
    collisionBlocks(bullets,blocks)
    collisionEnemies(bullets,enemies)

    if bullets:
        for bullet in bullets:
            bullet.update()
            bullet.render(display)


def collisionBlocks(bullets,blocks):
    for bullet in bullets[:]:
        for block in blocks:
            if bullet.bullet_rect.colliderect(block.block_rect):
                bullets.remove(bullet)
                break


def collisionEnemies(bullets,enemies):
    for bullet in bullets[:]:
        for enemy in enemies:
            if bullet.bullet_rect.colliderect(enemy.monster_lvl0_rect):
                enemy.health -= 100
                bullets.remove(bullet)
                break
        