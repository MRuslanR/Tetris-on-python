import time
import pygame
import random
import copy

pygame.init()

#ФПС
FPS=120
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

#Функция проеврки выхода за границы
def check_borders():
    if figure[i].x < 0 or figure[i].x > W - 1:
        return False
    elif figure[i].y > H - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True

#Игровой баланс
animation_speed=40
animation_limit=2400
animation_current=0

#Игровое поле, в котором будут отмечаться уже упавшие фигуры
field = [[0 for i in range(W)] for j in range(H+1)]


while True:
    #Цвет игрового поля
    screen.fill(pygame.Color('black'))
    dx = 0
    flag_rotate = False

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
            if event.key==pygame.K_UP:
                flag_rotate = True


    #Отрисовка сетки поля
    [pygame.draw.rect(screen, ("white"), i_rect, 1) for i_rect in grid]


    #Сдвиг фигуры вниз на 1 единицу при превышении лимита анимации
    animation_current+=animation_speed
    if animation_current>animation_limit:
        animation_current=0
        figure_old=copy.deepcopy(figure)
        for i in range(4):
            figure[i].y+=1
            if not check_borders():
                for i in range (4):
                    field[figure_old[i].y][figure_old[i].x] = pygame.Color('red') #mfidgjdjiejg
                figure=copy.deepcopy(figures[random.randint(0,6)])
                animation_limit = 2400
                break

    #Перемещение всех 4 квадратиков на dx c проверкой выхода за границу
    figure_old = copy.deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = copy.deepcopy(figure_old)
            break


    # переворот фигуры
    if flag_rotate == True and figures[1]!=figure:
        center = figure[0]
        figure_old = copy.deepcopy(figure)
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not check_borders():
                figure = copy.deepcopy(figure_old)
                break

    #Отрисовка фигуры путем рисования 4-х квадратиков
    for i in range(4):
        figure_rect.x = figure[i].x * SQUARE
        figure_rect.y = figure[i].y * SQUARE
        pygame.draw.rect(screen,('red'),figure_rect)

    #Проверка заполненности линии и сдвиг линий при полностью заполненной линии
    line = H - 1
    for i in range(H - 1, -1, -1):
        flag = True
        if all(field[i][j]!=0 for j in range (W)): flag = False
        field[line] = copy.deepcopy(field[i])
        if flag: line -= 1


    #Алгоритм отображения занятых клеток
    for y in range(H):
        for x in range(W):
            if field[y][x]:
                pygame.draw.rect(screen, 'red', (x*SQUARE,y*SQUARE,SQUARE-2,SQUARE-2))


    #Концовка игры
    if any(field[0][j]!=0 for j in range (W)):
        time.sleep(5)
        print("Конец игры")
        exit()

    #Обновление игрового экрана
    pygame.display.flip()
    clock.tick(FPS)

