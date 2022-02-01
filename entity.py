from abc import ABC, abstractmethod
import pygame
pygame.init()

class Entity(ABC):
    def __init__(self, x, y, w, color):
        self.x = x
        self.y = y
        self.w = w
        self.color = color

    def show(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.w))
        self.move()
        self.jump()
    
    @abstractmethod
    def move(self):
        pass