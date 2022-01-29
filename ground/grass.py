import pygame
from ground.ground import Ground
pygame.init()

class Grass(Ground):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)
        self.solid = True
        self.type = "GRASS"
    
    def draw(self, win):
        super().draw(win)