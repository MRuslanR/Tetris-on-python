import pygame
import random
import copy

pygame.init()

#Разрешение игры
RESOLUTION = 1920 * 1080
#ФПС
FPS=60
#Количество квадратиков-полей (горизонталь, вертикаль)
W, H = 10, 15
#Размеры квадратиков-поля
SQUARE=45


#Название игры
pygame.display.set_caption("Tetris from КНТ")
clock = pygame.time.Clock()

#Формируем экран из квадратиков
screen=pygame.display.set_mode((W*SQUARE,H*SQUARE))

#Создание иконки для приложения
icon = pygame.image.load('images/icon1.jpg')
pygame.display.set_icon(icon)


while True:
    #Цвет игрового поля
    screen.fill(pygame.Color('red'))

    #Выход из программы при закрытии окна
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    #Обновление игрового экрана
    pygame.display.update()
    clock.tick(FPS)