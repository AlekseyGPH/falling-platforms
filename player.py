from const import *
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(60,45))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 59)
        self.isJump = False
        self.jumpCount = 10
        self.speedx = 10
        self.upgrade = False
        self.upgrade_time = pygame.time.get_ticks()
        self.shield = False


    def update(self):
        self.calc_grav()
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
        if not(self.isJump):
            if keys[pygame.K_UP] and y > 5:
                self.rect.y -= speed
            if keys[pygame.K_DOWN]and y < 500 - height -15:
                self.rect.y += speed
        #прыжок
            if keys[pygame.K_SPACE]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) // 2
                else:
                    self.rect.y -= (self.jumpCount ** 2) // 2
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
        
    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            
	    self.change_y += .95
	    
	    # Если уже на земле, то ставим позицию Y как 0
	if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
	    self.change_y >= 0:
		self.change_y = 0
		self.rect.y = SCREEN_HEIGHT - self.rect.height
		self.change_y += .9               
                    self.change_y = 0
                    self.rect.y = SCREEN_HEIGHT - self.rect.height


