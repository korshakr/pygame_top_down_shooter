import conf

class Player:
    def __init__(self):
        self.image = conf.pygame.Surface((30,50))
        self.image.fill(conf.COLORS['RED'])
        self.player_rect = conf.pygame.Rect(conf.WINWIDTH // 2 - conf.X_CAMERA ,conf.WINHEIGHT // 2 - conf.Y_CAMERA,30,50)



    def check_collision(self,player,blocks):
        for block in blocks:
            if player.colliderect(block.get_rect()):
                return True

    def move(self,camera_pos,blocks):
        pos_x,pos_y = camera_pos

        key = conf.pygame.key.get_pressed()
        if key[conf.pygame.K_w]:
            self.player_rect.y -= 4
            pos_y += 4
            if self.check_collision(self.player_rect,blocks):
                self.player_rect.y += 4
                pos_y -= 4
        
        if key[conf.pygame.K_s]:
            self.player_rect.y += 4
            pos_y -= 4
            if self.check_collision(self.player_rect,blocks):
                self.player_rect.y -= 4
                pos_y += 4

        if key[conf.pygame.K_a]:
            self.player_rect.x -= 4
            pos_x += 4
            if self.check_collision(self.player_rect,blocks):
                self.player_rect.x += 4
                pos_x -= 4

        if key[conf.pygame.K_d]:
            self.player_rect.x += 4
            pos_x -= 4
            if self.check_collision(self.player_rect,blocks):
                self.player_rect.x -= 4
                pos_x += 4
       
        if self.player_rect.left < conf.BLOCKWIDTH:
            self.player_rect.x = conf.BLOCKWIDTH
            pos_x = camera_pos[0]
        
        if self.player_rect.right > conf.SURFACEWIDTH:
            self.player_rect.x = conf.SURFACEWIDTH - self.player_rect.width
            pos_x = camera_pos[0]

        if self.player_rect.top < conf.BLOCKHEIGHT:
            self.player_rect.y = conf.BLOCKHEIGHT
            pos_y = camera_pos[1]

        if self.player_rect.bottom > conf.SURFACEHIGHT:
            self.player_rect.y = conf.SURFACEHIGHT - self.player_rect.height
            pos_y = camera_pos[1]  

        

        return (pos_x,pos_y)

    
    def render(self,display):
        display.blit(self.image,self.player_rect)