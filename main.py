import pygame as pg
from pygame.locals import *
import sys
from random import randint

FPS = 60


class Game:
    clock = pg.time.Clock()

    def __init__(self):
        #Tamaño pantalla
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption('Arkanoid pyGame!')

        self.background_img = pg.image.load('resources/fondo.png').convert()
        
    def gameOver(self):
        pg.quit()
        sys.exit()
        
    def handleEvents(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.gameOver()
    
    def mainloop(self):
        while True:
            dt = self.clock.tick(FPS)
            
            self.handleEvents()
            self.screen.blit(self.background_img, (0,0))
            pg.display.flip()
            
    
if __name__ == '__main__':
    pg.init()
    game = Game()
    game.mainloop()