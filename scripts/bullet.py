import conf


from pygame.math import Vector2


class Bullet:
    def __init__(self,player_pos,angle):
        self.image = conf.pygame.Surface((10,10))
        self.image.fill(conf.COLORS['GREEN'])
        self.bullet_rect = self.image.get_rect(center=player_pos)

        self.pos = Vector2(player_pos)
        self.bullet_speed = Vector2(10,0).rotate(angle)


    def update(self):
        self.pos += self.bullet_speed
        self.bullet_rect.center = self.pos

        
    def render(self,display):
        display.blit(self.image,self.bullet_rect)



