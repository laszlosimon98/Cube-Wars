from abc import abstractclassmethod, abstractmethod
import pygame
pygame.init()

class Ground:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))
    
    def isSolid(self):
        return self.solid

    def getType(self):
        return self.type