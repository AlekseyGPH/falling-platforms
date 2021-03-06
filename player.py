from const import *
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(60,45))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 56
        self.isJump = False
        self.jumpCount = PLAYER_JUMP_COUNT
        self.speedx = 6
        self.speedy = 1




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
        if not self.isJump:
            if keys[pygame.K_UP] and self.rect.y > 5:
                self.rect.y -= SPEED
            if keys[pygame.K_DOWN]and self.rect.y < 500 - SCREEN_HEIGHT -15:
                self.rect.y += SPEED
        #прыжок
            if keys[pygame.K_SPACE]:
                self.isJump = True
        else:
            #если прыжок не закончен
            if self.jumpCount >= -PLAYER_JUMP_COUNT:
                
                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) // 2
                elif self.jumpCount >= 0:
                    self.rect.y -= (self.jumpCount ** 2) // 2
                self.jumpCount -= 1
            # прыжок закончен
            else:
                self.isJump = False
                self.jumpCount = PLAYER_JUMP_COUNT
        





























                                
   
