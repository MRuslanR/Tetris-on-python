import pygame
import random
import copy

pygame.init()

#ФПС
FPS=60
#Количество квадратиков-полей (горизонталь, вертикаль)
W, H = 10, 15
#Размеры квадратиков-поля
SQUARE=45

#Название игры
pygame.display.set_caption("Tetris from КНТ")
#Создание игрового таймера
clock = pygame.time.Clock()

#Формируем экран из квадратиков
screen=pygame.display.set_mode((W*SQUARE,H*SQUARE))

#Создание иконки для приложения
icon = pygame.image.load('images/icon1.jpg')
pygame.display.set_icon(icon)

#Создание сетки поля, rect() отвечает за координаты квадрата. 1-коорд по х 2-коорд по у 3-размер первой стороны 4-размер второй стороны
grid = [pygame.Rect(x*SQUARE,y*SQUARE,SQUARE,SQUARE) for x in range (W) for y  in range(H)]

#Создание всех 7 фигур. 1 координата в каждом из 7 подмассивов отвечает за центр вращения фигуры
figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

#Создание фигур, фигура появляется в центре W, центр вращения на 1 клетку ниже
figures = [[pygame.Rect(x + W//2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
#Объект, отвечающий за отрисовку квадратика. -2 для того, чтобы квадратик не перерисовывал стенки
figure_rect = pygame.Rect(0, 0, SQUARE - 2, SQUARE - 2)

figure=copy.deepcopy(random.choice(figures))

#Функция проеврки выхода за границу W

#cur = figure[i]
def check_bordersX(cur):
    if cur.x < 0 or cur.x > W - 1:
        return False
    return True
def check_bordersY(cur):
    if cur.y > H - 1 or field[cur.y][cur.x]!=0:
        return False
    return True

animation_speed=160
animation_limit=2400
animation_current=0
#Игровое поле, в котором будут отмечаться уже упавшие фигуры
field = [[0 for i in range(W)] for i in range(H)]

while True:
    #Цвет игрового поля
    screen.fill(pygame.Color('black'))
    dx = 0


    #Выход из программы при закрытии окна
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        #Отслеживание перемещения фигуры влево вправо
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                dx-=1
            if event.key==pygame.K_RIGHT:
                dx+=1
            if event.key==pygame.K_DOWN:
                animation_limit=160



    #Перемещение всех 4 квадратиков на dx c проверкой выхода за границу
    figure_old = copy.deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_bordersX(figure[i]):
            figure = copy.deepcopy(figure_old)
            break
    #Отрисовка сетки поля
    [pygame.draw.rect(screen, ("white"), i_rect, 1) for i_rect in grid]

    #Сдвиг фигуры вниз на 1 единицу при превышении лимита анимации
    animation_current+=animation_speed
    if animation_current>animation_limit:
        animation_current=0
        figure_old=copy.deepcopy(figure)
        for i in range(4):
            figure[i].y+=1
            if not check_bordersY(figure[i]):
                for j in range (4):
                    field[figure_old[j].y][figure_old[j].x]=pygame.Color("White") #mfidgjdjiejg
                animation_limit=2400
                figure=copy.deepcopy(random.choice(figures))
                break





    #Отрисовка фигуры путем рисования 4-х квадратиков
    for i in range(4):
        figure_rect.x = figure[i].x * SQUARE
        figure_rect.y = figure[i].y * SQUARE
        pygame.draw.rect(screen,('red'),figure_rect)

 #IODIWHDHWIDHIWHD
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                figure_rect.x, figure_rect.y = x * SQUARE, y * SQUARE
                pygame.draw.rect(screen, col, figure_rect)


    #Обновление игрового экрана
    pygame.display.flip()
    clock.tick(FPS)

