import pygame
import random

from settings import *

class Background:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.bcg = BACKGROUND
        self.stars_color = STARCOLOR
        self.radius = RADIUS
        self.stars = []
    
    def generate_stars(self):
        if len(self.stars) < STARSCOUNT:
            x = random.randrange(0, self.w)
            y = random.randrange(-100, self.h - 100)
            self.stars.append([x, y])

    def draw(self, win):
        win.fill(self.bcg)
        self.generate_stars()
        for i in range(len(self.stars)):
            pygame.draw.circle(win, self.stars_color, (self.stars[i][0], self.stars[i][1]), self.radius)
            self.stars[i][1] += 1
            if (self.stars[i][1] > self.h - HEIGHT - self.radius / 2):
                self.stars.pop(i)
                self.generate_stars()