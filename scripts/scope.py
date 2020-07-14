import conf

class Scope:
    def __init__(self):
        self.image = conf.pygame.Surface((0,0))
        self.point_rect = conf.pygame.Rect(0,0,0,0)


    def set_values(self,camera_pos):
        x_cursor, y_cursor = conf.pygame.mouse.get_pos()
        self.image = conf.pygame.Surface((10,10))
        self.image.fill(conf.COLORS['GREEN'])
        self.point_rect = conf.pygame.Rect(x_cursor - camera_pos[0],y_cursor - camera_pos[1],10,10)


    def set_default(self):
        self.image = conf.pygame.Surface((0,0))
        self.point_rect = conf.pygame.Rect(0,0,0,0)


    def render(self,display):
        display.blit(self.image,self.point_rect)