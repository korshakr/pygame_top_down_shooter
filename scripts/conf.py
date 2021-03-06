import pygame
from pygame.locals import *

pygame.init()

FPS = 40


WINWIDTH = 1024
WINHEIGHT = 860


SURFACEWIDTH = 2000
SURFACEHIGHT = 2000

X_CAMERA = WINWIDTH // 2 - 10
Y_CAMERA = WINHEIGHT // 2 - 10


BLOCKWIDTH = 5
BLOCKHEIGHT = 5

COLORS = {

    'BLACK' : (0,0,0),
    'BLUE'  : (0,0,255),
    'DARK_GREEN' : (0,51,0),
    'GREEN' : (0,204,0),
    'RED'   : (255,0,0),
    'WHITE' : (255,255,255),
    'YELLOW': (255,255,0),
}

