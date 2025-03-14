import pygame

class Weapon:
    def __init__(self, path_image_weapon):
        pygame.image.load(path_image_weapon).convert_alpha()

