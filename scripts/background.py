import conf
from player import Player
from wall import Block
from scope import Scope

def draw_map(display):
    world = conf.pygame.Surface((conf.SURFACEWIDTH,conf.SURFACEHIGHT))
    # world.fill(conf.COLORS['WHITE'])

    player = Player()
    scope = Scope()

    camera_pos = (conf.X_CAMERA,conf.Y_CAMERA)

    blocks = createBlocks(world)
    # for block in blocks:
    #     block.render(world)

    while True:
        for event in conf.pygame.event.get():
            if event.type == conf.pygame.QUIT:
                return

            if event.type == conf.pygame.MOUSEBUTTONUP:
                scope.set_values(camera_pos)
                

        camera_pos = player.move(camera_pos,blocks)
        

        display.fill(conf.COLORS['BLACK'])
        world.fill(conf.COLORS['WHITE'])

        for block in blocks:
            block.render(world)


       

        player.render(world)
        scope.render(world)
        
        display.blit(world,camera_pos)

        conf.pygame.display.flip()


def createBlocks(world):
    blocks = []
    for x in range(0,800,5):
        blocks.append(Block(x,0))
        

    for y in range(0,801,5):
        for x in [0,800]:
            blocks.append(Block(x,y))
            
    

    for x in range(0,800,5):
        if x in range(530,581):
            continue
        blocks.append(Block(x,800))

    return blocks
        
    
    