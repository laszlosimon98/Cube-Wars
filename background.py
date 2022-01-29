import pygame
import random

from settings import *

class Background:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.stars = STARSCOUNT
        self.bcg = BACKGROUND
        self.stars_color = STARCOLOR
        self.radius = RADIUS
    
    def draw(self, win):
        win.fill(self.bcg)
        for i in range(self.stars):
            x = random.randrange(0, self.w)
            y = random.randrange(0, self.h)
            pygame.draw.circle(win, self.stars_color, (x, y), self.radius)