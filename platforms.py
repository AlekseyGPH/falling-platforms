from const import *
import pygame
from random import randint

class Platforms(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/ground1.png").convert()
        self.image = pygame.transform.scale(self.image, (480,56))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.speedy = 2
        self.score = 0
    
    def update(self):
        if self.rect.top >= SCREEN_HEIGHT:
            self.rect.left = randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.bottom = 0
            self.score += 1
