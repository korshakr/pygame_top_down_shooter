import conf
import background

def main():
    background.draw_map(windowSurface,conf.FPS)




if  __name__ == "__main__":
    windowSurface = conf.pygame.display.set_mode((conf.WINWIDTH,conf.WINHEIGHT)) 
    main()