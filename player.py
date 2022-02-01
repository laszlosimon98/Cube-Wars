from entity import Entity
from settings import PLAYERVEL, SCREEN_HEIGHT, SCREEN_WIDTH
import math
import pygame
pygame.init()

class Player(Entity):
    def __init__(self, x, y, w, color):
        super().__init__(x, y, w, color)
        self.isjump = False
        self.isfalling = False
        self.jump_count = 16
        self.jump_height = self.jump_count
        self.on_platforms = []

    def move(self):
        key = pygame.key.get_pressed()

        if (key[pygame.K_a]) and self.x > 0:
            self.x -= PLAYERVEL
        elif (key[pygame.K_d]) and self.x + self.w < SCREEN_WIDTH:
            self.x += PLAYERVEL

        if (key[pygame.K_w] or key[pygame.K_SPACE]) and not self.isjump:
            self.isjump = True

        if (key[pygame.K_s]):
            self.jump_count = 0
            self.isjump = True

        for i, p in enumerate(self.on_platforms):
            distance = math.sqrt(math.pow(self.y + self.w - p.get_y(), 2))
            if (distance < 2 and (self.x + self.w < p.get_x() or self.x > p.get_x() + p.get_w())):
                self.jump_count = 0
                self.isjump = True
    
    def jump(self):
        if self.isjump:
            if self.jump_count > 0:
                self.y -= self.jump_count ** 2 * 0.1
                self.jump_count -= 1
            elif self.jump_count == 0:
                self.falling(self.calc_distance(self.on_platforms))
    
    def calc_distance(self, arr):
        _min = SCREEN_HEIGHT
        for i in range(0, len(arr)):
            if arr[i].get_y() < _min and arr[i].get_y() != self.y + self.w:
                _min = arr[i].get_y()
        distance = math.pow(self.y + self.w - _min, 2)
        return (math.sqrt(distance), _min)
    
    def falling(self, distance):
        if (distance[0] > 5):
            self.y += 5
        else:
            self.jump_count = self.jump_height
            self.isjump = False
            self.y = distance[1] - self.w

    
    def is_on_platform(self, platforms):
        for _, p in enumerate(platforms):
            if (p not in self.on_platforms):
                if (self.x + self.w >= p.get_x() and self.x <= p.get_x() + p.get_w() and self.y + self.w <= p.get_y()):
                    self.on_platforms.append(p)
            else:
                if (self.x + self.w < p.get_x() or self.x > p.get_x() + p.get_w() or self.y + self.w > p.get_y()):
                    self.on_platforms.remove(p)
