from pygame import *
from pygame.locals import *
import sys
from random import randint
from entities import *

init()


class Game:
    clock = time.Clock()

    def __init__(self):
        self.screen = display.set_mode((800, 600))
        display.set_caption('Hola mundo!')

        self.background_color = (150, 150, 222)