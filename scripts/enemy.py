import conf

class Enemy:
    def __init__(self):
        self.health = 101
        self.damage = 10
        self.speed = 2



class monster_lvl0(Enemy):
    def __init__(self):
        super().__init__()

        self.image = conf.pygame.Surface((30,50))
        self.image.fill(conf.COLORS['DARK_GREEN'])
        self.monster_lvl0_rect = conf.pygame.Rect(600,1000,30,50)

    def render(self,display):
        display.blit(self.image,self.monster_lvl0_rect)