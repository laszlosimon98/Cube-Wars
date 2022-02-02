from entity import Entity
from settings import *
from ground.lava import Lava
from ground.water import Water
from bullet import Bullet
import math
import pygame
pygame.init()

class Player(Entity):
    def __init__(self, x, y, w, color):
        super().__init__(x, y, w, color)
        self.isjump = False
        self.jump_count = 16
        self.jump_height = self.jump_count
        self.on_platforms = []
        self.in_water = False
        self.in_lava = False
        self.bullets = []
    
    def get_bullets(self):
        return self.bullets

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a] and self.x > 0 and not self.in_lava:
            self.x -= PLAYERVEL
        elif key[pygame.K_d] and self.x + self.w < SCREEN_WIDTH and not self.in_lava:
            self.x += PLAYERVEL

        if key[pygame.K_w] or key[pygame.K_SPACE] and not self.isjump:
            self.isjump = True

        if key[pygame.K_s]:
            if self.y + self.w < SCREEN_HEIGHT - HEIGHT:
                self.fall()

        if len(self.on_platforms) == 0 and not self.isjump:
            self.fall()
    
    def shoot(self, pos):
        bullet = Bullet(self.x + self.w / 2, self.y + self.w / 2, BULLETRADIUS, PLAYERCOLOR)
        direction = math.atan2(pos[0] - self.x - self.w / 2, pos[1] - self.y - self.w / 2)
        bullet.update(math.sin(direction), math.cos(direction))
        self.bullets.append(bullet)
                
    def fall(self):
        self.jump_count = 0
        self.isjump = True
    
    def jump(self):
        if self.isjump:
            if self.jump_count > 0:
                self.y -= self.jump_count ** 2 * 0.15
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
        if distance[0] > FALLSPEED:
            if not self.in_water and not self.in_lava:
                self.y += FALLSPEED
            elif self.in_water:
                self.y += FALLSPEEDWL
                self.isjump = False
                self.jump_count = self.jump_height
            elif self.in_lava:
                    self.y += FALLSPEEDWL
        else:
            if not self.in_lava:
                self.jump_count = self.jump_height
                self.isjump = False
            self.y = distance[1] - self.w

    
    def is_on_platform(self, platforms):
        for _, p in enumerate(platforms):
            distance = math.sqrt(math.pow(self.y + self.w - p.get_y(), 2))
            if p not in self.on_platforms:
                if self.x + self.w >= p.get_x() and self.x <= p.get_x() + p.get_w() and distance < FALLSPEED:
                    if type(p) != Lava and type(p) != Water:
                        self.on_platforms.append(p)
                    self.in_water = type(p) == Water
                    self.in_lava = type(p) == Lava and len(self.on_platforms) == 0
            else:
                if self.x + self.w < p.get_x() or self.x > p.get_x() + p.get_w() or distance >= FALLSPEED:
                    self.on_platforms.remove(p)
