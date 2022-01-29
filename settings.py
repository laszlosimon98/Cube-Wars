import pygame
pygame.init()

FPS = 30
STARSCOUNT = 30

# Stars
BACKGROUND = (135, 206, 235) # sky color
STARCOLOR = (255, 255, 255)
RADIUS = 3

# Platfrom

GRASS = (161, 223, 80)
ICE = (219, 241, 253)
SWAMP = (82, 100, 29)
WATER = (2, 75, 134)
LAVA = (207, 16, 32)

SMALL = pygame.display.Info().current_w / 5
MEDIUM = pygame.display.Info().current_w / 3
LARGE = pygame.display.Info().current_w / 2
HEIGHT = 50