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

#Создание сетки поля, rect() отвечает за координаты квадрата
grid = [pygame.Rect(x*SQUARE,y*SQUARE,SQUARE,SQUARE) for x in range (W) for y  in range(H)]

#Создание всех 7 фигур. 1 координата в каждом из 7 подмассивов отвечает за центр вращения фигуры
figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, SQUARE - 2, SQUARE - 2)

figure=figures[3]
while True:
    #Цвет игрового поля
    screen.fill(pygame.Color('black'))

    #Выход из программы при закрытии окна
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    #Отрисовка сетки поля
    [pygame.draw.rect(screen, ("white"), i_rect, 1) for i_rect in grid]

    for i in range(4):
        figure_rect.x=figure[i].x*SQUARE
        figure_rect.y = figure[i].y * SQUARE
        pygame.draw.rect(screen,('red'),figure_rect)

    #Обновление игрового экрана
    pygame.display.flip()
    clock.tick(FPS)