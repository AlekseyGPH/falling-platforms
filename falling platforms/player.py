from const import *
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/stickman.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image,(60,45))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.upgrade = False
        self.upgrade_time = pygame.time.get_ticks()
        self.shield = False

    def update(self):
        keys = pygame.key.get_pressed()
        #если нажата стрелка вниз
        if keys[pygame.K_LEFT]:
        #изменяем координату x прямоугольника
            self.rect.x -= self.speedx
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        #если вышел за границу экрана, то возврат на эту границу
        #левая граница
        if self.rect.left <= 0:
            self.rect.left = 0
        #правая граница
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH





