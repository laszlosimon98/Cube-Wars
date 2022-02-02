from settings import BULLETVEL
import pygame
pygame.init()

class Bullet:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.x_dir = 0
        self.y_dir = 0
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.r)
    
    def update(self, x, y):
        self.x_dir = x * BULLETVEL
        self.y_dir = y * BULLETVEL
    
    def move(self):
        self.x += self.x_dir
        self.y += self.y_dir