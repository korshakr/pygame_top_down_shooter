import conf

class Block:
    def __init__(self,left,top):
        self.image = conf.pygame.Surface((conf.BLOCKWIDTH,conf.BLOCKHEIGHT))
        self.image.fill(conf.COLORS['BLUE'])
        self.block_rect = conf.pygame.Rect(left, top, conf.BLOCKWIDTH, conf.BLOCKHEIGHT)


    def get_rect(self):
        return self.block_rect

        
    def render(self,display):
        display.blit(self.image,self.block_rect)