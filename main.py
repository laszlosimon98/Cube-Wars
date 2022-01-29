import enum
import pygame
from background import Background

# settings
from settings import *

# background
from background import Background

# ground
from ground.grass import Grass
from ground.ice import Ice
from ground.swamp import Swamp
from ground.water import Water
from ground.lava import Lava

pygame.init()

class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.win = pygame.display.set_mode((1000, 600))
        self.w = pygame.display.Info().current_w
        self.h = pygame.display.Info().current_h
        self.title = pygame.display.set_caption("Cube Wars")
        self.clock = pygame.time.Clock()
        self.run = True

        self.background = Background(self.w, self.h)

        
        self.swamps = [
            Swamp(SMALL, self.h - HEIGHT, SMALL, HEIGHT, SWAMP),
            Swamp(self.w - 2*SMALL, self.h - HEIGHT, SMALL, HEIGHT, SWAMP)
        ]

        self.waters = [
            Water(0, self.h - HEIGHT, SMALL, HEIGHT, WATER),
            Water(self.w - SMALL, self.h - HEIGHT, SMALL, HEIGHT, WATER),
        ]

        self.lavas = [
            Lava(self.w / 2 - SMALL / 2, self.h - HEIGHT, SMALL, HEIGHT, LAVA)
        ]

    def setup(self):
        self.background.draw(self.win)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            key = pygame.key.get_pressed()
            if(key[pygame.K_ESCAPE]):
                self.run = False

            self.draw(self.win)

    def show(self, win, platform):
        for _, p in enumerate(platform):
            p.draw(win)

    def draw(self, win):
        self.show(win, self.swamps)
        self.show(win, self.waters)
        self.show(win, self.lavas)

        self.clock.tick(FPS)
        pygame.display.update()

if __name__ == "__main__":
    g = Game()
    g.setup()
