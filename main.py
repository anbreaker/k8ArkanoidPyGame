import pygame as pg
from pygame.locals import *
import sys
from random import randint
from entities import *

FPS = 60


class Game:
    clock = pg.time.Clock()

    def __init__(self):
        # Tamaño pantalla
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption('Arkanoid pyGame!')

        self.background_img = pg.image.load(
            'resources/background.png').convert()
        # self.player = Racket(100,295) #Para enredar y comprobar en distinta posicion de Racket
        self.player = Racket()
        self.ball = Ball()

        self.playerGroup = pg.sprite.Group()
        self.allSprites = pg.sprite.Group()
        self.playerGroup.add(self.player)
        self.allSprites.add(self.player)
        self.allSprites.add(self.ball)

    def gameOver(self):
        pg.quit()
        sys.exit()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.gameOver()

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.player.go_left()

                if event.key == K_RIGHT:
                    self.player.go_right()

        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.player.go_left()

        if keys_pressed[K_RIGHT]:
            self.player.go_right()

    def mainloop(self):
        while True:
            dt = self.clock.tick(FPS)

            self.handleEvents()

            # Comprobar choques con Racket
            self.ball.test_collision(self.playerGroup)
            if self.ball.speed == 0:  # Se produce colision
                # Quitar vida a player
                self.player.lives -= 1
                # Inicio de una nueva bola, avisar a bola que vuelva al inicio (metodo)
                self.ball.start()

            if self.player.lives == 0:
                self.gameOver()

            self.screen.blit(self.background_img, (0, 0))

            self.allSprites.update(dt)
            self.allSprites.draw(self.screen)

            pg.display.flip()


if __name__ == '__main__':
    pg.init()
    game = Game()
    game.mainloop()
