import pygame
from ground.ground import Ground
pygame.init()

class Water(Ground):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)
        self.solid = False 
        self.type = "WATER"
    
    def draw(self, win):
        super().draw(win)
