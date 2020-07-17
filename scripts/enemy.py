import conf

# from pygame.math import Vector2

import math

class Enemy:
    def __init__(self):
        self.health = 101
        self.damage = 10
        self.speed = 3
        self.range_zone = 200
        self.range_zone_image = conf.pygame.Surface((self.range_zone * 2,self.range_zone * 2))
        self.zone_rect = None

    def draw_range_zone(self,display,centre_enemy):
        self.range_zone_image.set_alpha(128)
        centre_enemy = (centre_enemy[0] - self.range_zone,centre_enemy[1] - self.range_zone)
        self.zone_rect = conf.pygame.Rect(centre_enemy[0],centre_enemy[1],self.range_zone * 2, self.range_zone * 2)
        display.blit(self.range_zone_image,centre_enemy)


class monster_lvl0(Enemy):
    def __init__(self):
        super().__init__()
        
        self.image = conf.pygame.Surface((30,50))
        self.image.fill(conf.COLORS['DARK_GREEN'])
        self.monster_lvl0_rect = conf.pygame.Rect(800,1000,30,50)

    def define_status(self,player,blocks):
        if player.player_rect.colliderect(self.zone_rect):
             self.range_zone_image.fill(conf.COLORS['RED'])
             self.warning_mode(player,blocks)
        else:
            self.range_zone_image.fill(conf.COLORS['GREEN'])
            self.standard_mode()
   

    def normalize_vector(self,vector):
        if vector == [0,0]:
            return [0,0]
        else:
            path = math.sqrt(math.pow(vector[0],2) + math.pow(vector[1],2))
            return (vector[0] / path, vector[1] / path)

    def collision(self,blocks):
        for block in blocks:
            if self.monster_lvl0_rect.colliderect(block.block_rect):
                return True
        return False

    def standard_mode(self):
        pass


    def warning_mode(self,player,blocks):

        if self.collision(blocks):
          self.monster_lvl0_rect.centerx -= self.moveVector[0] * self.speed
          self.monster_lvl0_rect.centery -= self.moveVector[1] * self.speed
        else:
            self.moveVector = (player.player_rect.topleft[0] - self.monster_lvl0_rect.centerx,
                          player.player_rect.topleft[1] - self.monster_lvl0_rect.centery)
            
            self.moveVector = self.normalize_vector(self.moveVector)
            self.monster_lvl0_rect.centerx += self.moveVector[0] * self.speed
            self.monster_lvl0_rect.centery += self.moveVector[1] * self.speed

        
    def render(self,display,player,blocks):
       
        display.blit(self.image,self.monster_lvl0_rect)
        self.draw_range_zone(display,self.monster_lvl0_rect.center)
        self.define_status(player,blocks)