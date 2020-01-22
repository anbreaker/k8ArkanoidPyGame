import pygame as pg
from pygame.locals import *
import sys
from entities import *

FPS = 60
WHITE = (255,255,255)


class Game:
    clock = pg.time.Clock()
    score = 0

    def __init__(self):
        # Tamaño pantalla
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption('Arkanoid pyGame!')

        self.background_img = pg.image.load(
            'resources/background.png').convert()
        self.font = pg.font.Font('resources/fonts/font.ttf', 22)
        self.marcador = self.font.render('0', True, WHITE)
        self.livesCounter = self.font.render('0', True, WHITE)

        # self.player = Racket(100,295) #Para enredar y comprobar en distinta posicion de Racket
        self.player = Racket()
        self.ball = Ball()

        self.tileGroup = pg.sprite.Group()
        for j in range(5):
            for i in range(16):
                t = Tile(i*50, 60+j*32)
                self.tileGroup.add(t)

        self.playerGroup = pg.sprite.Group()
        self.allSprites = pg.sprite.Group()
        self.playerGroup.add(self.player)
        self.allSprites.add(self.player)
        self.allSprites.add(self.ball)
        self.allSprites.add(self.tileGroup)
        self.score = 0

    def quitGame(self):
        pg.quit()
        sys.exit()
        
    def gameOver(self):
        pass

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.quitGame()

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
            self.ball.test_collisions(self.playerGroup)
            self.score += self.ball.test_collisions(self.tileGroup, True)            

            print(self.score)

            if self.ball.speed == 0:  # Se produce colision
                # Quitar vida a player
                self.player.lives -= 1
                # Inicio de una nueva bola, avisar a bola que vuelva al inicio (metodo)
                self.ball.start()                

            if self.player.lives == 0:
                self.quitGame()
                

            self.livesCounter = self.font.render(str(self.player.lives), True, WHITE)
            self.marcador = self.font.render(str(self.score), True, WHITE)
            
            self.screen.blit(self.background_img, (0, 0))

            self.allSprites.update(dt)
            self.allSprites.draw(self.screen)
            
            self.screen.blit(self.marcador, (750,10))
            self.screen.blit(self.livesCounter, (50,10))

            pg.display.flip()


if __name__ == '__main__':
    pg.init()
    game = Game()
    game.mainloop()
