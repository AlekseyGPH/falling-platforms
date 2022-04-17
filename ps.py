from const import *
import pygame
from random import randint
from player import Player
from platforms import Platforms

class Platformssmall(pygame.sprite.Sprite):
    def __init__(self, x = 150, y = 600):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/ground.jpg").convert()
        self.image = pygame.transform.scale(self.image, (170,30))
        self.rect = self.image.get_rect()
        #self.rect.left = randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.x = x
        self.rect.bottom = y
        self.speedy = 2
        self.score = 0
        player = Player()
        
    def update(self):
        pass
##        hits = pygame.sprite.spritecollide(player, ps, platforms, False)
##        for hit in hits:
##            if player.rect.centery > hit.rect.top:
##                player.rect.bottom = hit.rect.top
##                player.speedy = 0
##        if self.rect.top >= SCREEN_HEIGHT:
##            self.rect.left = randint(0, SCREEN_WIDTH - self.rect.width)
##            self.rect.bottom = 0
##            self.score += 1
