import pygame
from ground.ground import Ground
pygame.init()

class Swamp(Ground):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)
    
    def draw(self, win):
        super().draw(win)