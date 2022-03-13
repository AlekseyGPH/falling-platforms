# подключаем модули
import pygame
import sys
from random import randint
from const import *
from platforms import Platforms
from bg import Background
from player import Player

#НАСТРОЙКА ИГРЫ (ИНИЦИАЛИЗАЦИЯ)
#инициализация библиотеки
pygame.init()
#создание экрана, указываем ширину и высоту в кортеже
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# создаем часы для отслеживания FPS
clock = pygame.time.Clock()
# ПЕРЕМЕННЫЕ
# переменная для управления циклом
run = True
#СПРАЙТЫ И ГРУППЫ
#создание групп
all_sprites = pygame.sprite.Group()
#создаём группу (список) для препятствий
platforms = pygame.sprite.Group()
#создание игровых объектов
platforms1 = Platforms(720)#здесь вызовется init и объект создастся
platforms2 = Platforms(-240)
player = Player()
bg1 = Background(0,0)
bg2 = Background(0,-SCREEN_HEIGHT)
#добавление в группы
all_sprites.add(bg1)
all_sprites.add(bg2)
all_sprites.add(player)
all_sprites.add(platforms1)
all_sprites.add(platforms2)
platforms.add(platforms1)
platforms.add(platforms2)
# основной игровой цикл
while run:
    #0 задержка для фиксированного FPS
    clock.tick(FPS)
    #1 обработка событий
    for event in pygame.event.get():
        # если тип события - закрытие окна программы
        if event.type == pygame.QUIT:
            # выйти из программы
            run = False
#2 действия и взаимодействия
    all_sprites.update()
    #проверка столкновений
#3 отрисовка
    screen.fill(GREY)
    all_sprites.draw(screen)
    pygame.display.update()

#здесь основной цикл игры закончился
# завершить pygame
pygame.quit()
# выйти
sys.exit()




























