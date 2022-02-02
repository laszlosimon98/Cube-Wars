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

# player
from player import Player

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
        self.bullet = None

        self.background = Background(self.w, self.h)

        self.platforms = [
            Grass(self.w - SMALL / 3 - 50, HEIGHT + PLAYERSIZE, SMALL / 3, HEIGHT, GRASS), # startpoint

            Grass(0 + SMALL, self.h - HEIGHT, SMALL, HEIGHT, GRASS),
            Grass(0, self.h - HEIGHT * 3.5, MEDIUM, HEIGHT, GRASS),
            Grass(self.w - MEDIUM, self.h - HEIGHT * 3.5, MEDIUM, HEIGHT, GRASS),

            Ice(MEDIUM + SMALL / 2 + 20, self.h - HEIGHT * 3.5, SMALL / 2, HEIGHT, ICE),

            Swamp(SMALL, self.h - HEIGHT, SMALL, HEIGHT, SWAMP),
            Swamp(self.w - 2 * SMALL, self.h - HEIGHT, SMALL, HEIGHT, SWAMP),

            Water(0, self.h - HEIGHT, SMALL, HEIGHT, WATER),
            Water(self.w - SMALL, self.h - HEIGHT, SMALL, HEIGHT, WATER),

            Lava(self.w / 2 - SMALL / 2, self.h - HEIGHT, SMALL, HEIGHT, LAVA),
        ]

        self.player = Player((self.w - SMALL / 3 - 25) + PLAYERSIZE / 2, HEIGHT, PLAYERSIZE, PLAYERCOLOR)

    def setup(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.player.shoot(pos)

            key = pygame.key.get_pressed()
            if(key[pygame.K_ESCAPE]):
                self.run = False
            
            self.player.is_on_platform(self.platforms)

            for _, b in enumerate(self.player.get_bullets()):
                b.move()

            self.draw(self.win)

    def show(self, win, platform):
        for _, p in enumerate(platform):
            p.draw(win)

    def draw(self, win):
        self.background.draw(self.win)
        self.show(win, self.platforms)
        self.player.draw(win)

        for _, b in enumerate(self.player.get_bullets()):
            b.draw(win)

        self.clock.tick(FPS)
        pygame.display.update()

if __name__ == "__main__":
    g = Game()
    g.setup()
