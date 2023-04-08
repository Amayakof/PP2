<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import pygame, sys
from datetime import datetime
import math
=======
import pygame
import random
import sys


# Размеры окна в пикселях
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

CELL_SIZE = 20

# Размеры сетки в ячейках
WIDTH = int(WINDOW_WIDTH / CELL_SIZE)
HEIGHT = int(WINDOW_HEIGHT / CELL_SIZE)

# Цвета
BG_COLOR = (0, 0, 0)
GRID_COLOR = (40, 40, 40)
APPLE_COLOR = (255, 0, 0)
APPLE_OUTER_COLOR = (155, 0, 0)
SNAKE_COLOR = (0, 255, 0)
SNAKE_OUTER_COLOR = (0, 155, 0)


UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0


FPS = 15

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
>>>>>>> 13f344a (git push)


def main():
    global FPS_CLOCK
    global DISPLAY

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Wormy')

    while True:
        # Мы всегда будем начинать игру с начала. После проигрыша сразу
        # начинается следующая.
        run_game()


def run_game():
    # TODO(2.1): создать яблоко в позиции (20, 10)

    # TODO(3.1): создать змейку. Пусть она состоит из трех ячеек
    #  в строке 10 и столбцах 3, 4, 5.
    #  Какой тип данных удобен для представления змейки?

    # TODO(4.1): задать исходное направление движения змейки.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            # TODO(7.1): обработайте событие pygame.KEYDOWN
            #  и при необходимости измените направление движения змейки.

        # TODO(5.1): если змейка достигла границы окна, завершить игру.
        #  Для проверки воспользуйтесь функцией snake_hit_edge.

        # TODO(8.1): если змейка задела свой хвост, завершить игру.
        #  Для проверки восппользуйтесь функцией snake_hit_self.

        # TODO(6.1): обработайте ситуацию столкновения змейки с яблоком.
        #  В этом случае нужно:
        #  * Увеличить размер змейки
        #  * Создать новое яблоко.

        # TODO(4.2): сдвинуть змейку в заданном направлении
        # TODO(2.2): передать яблоко в функцию отрисовки кадра
        # TODO(3.2): передать змейку в функцию отрисовки кадра
        draw_frame(None, None)
        FPS_CLOCK.tick(FPS)


<<<<<<< HEAD
if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
=======
import pygame
=======
import pygame, sys
from datetime import datetime
import math
>>>>>>> d8c3d6c (git pull)


def main():

    # pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    # get the current time
    curr_time = datetime.now()
    curr_sec = curr_time.second
    curr_min = curr_time.minute


    # loading the images 
    clock_image = pygame.transform.scale(pygame.image.load('./images/mickeyclock.jpeg'), (800, 600))
    sechand_image = pygame.image.load('./images/sechand.png')
    sechand_image = pygame.transform.scale(sechand_image, (250, 75))
    sechand_rect = sechand_image.get_rect()
    sechand_rect.center = (400, 300)
    minhand_image = pygame.image.load('./images/minhand.png')
    minhand_image = pygame.transform.scale(minhand_image, (200, 50))
    minhand_rect = minhand_image.get_rect()
    minhand_rect.center = (400, 300)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
        screen.fill(0)
        screen.blit(clock_image, (0, 0))
    
        rot_minhand = pygame.transform.rotate(minhand_image, -1 * (6 * curr_min) - 160)
        rot_minhand_rect = rot_minhand.get_rect()
        rot_minhand_rect.center = minhand_rect.center
        screen.blit(rot_minhand, rot_minhand_rect)
    
        rot_sechand = pygame.transform.rotate(sechand_image, -1 * (6 * curr_sec) + 90)
        rot_sechand_rect =rot_sechand.get_rect()
        rot_sechand_rect.center = sechand_rect.center
        screen.blit(rot_sechand, rot_sechand_rect)

<<<<<<< HEAD
    pygame.display.flip()
    
pygame.quit()
exit()
>>>>>>> 7bca860 (git pull)
=======
        curr_time = datetime.now()
        curr_sec = curr_time.second
        curr_min = curr_time.minute
        
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
>>>>>>> d8c3d6c (git pull)
=======
def draw_frame(snake, apple):
    DISPLAY.fill(BG_COLOR)
    draw_grid()
    draw_snake(snake)
    draw_apple(apple)
    pygame.display.update()


def draw_grid():
    # TODO(1.2): нарисовать сетку.
    #  Шаг CELL_SIZE
    #  Цвет GRID_COLOR
    #  https://www.pygame.org/docs/ref/draw.html#pygame.draw.line
    ...


def draw_apple(apple):
    # TODO(2.3): нарисовать яблоко.
    ...


def draw_snake(snake):
    # TODO(3.3): нарисовать змейку.
    ...


def draw_cell(cell, outer_color, inner_color):
    # TODO(2.4): вспомогательная функция для рисования ячейки.
    #  Ячейка будет состоять из двух квадратов разных цветов:
    #  Больший квадрат закрашивается цветом outer_color,
    #  меньший - inner_color.
    #  Расстояние между внешним и внутренним квадратом
    #  принять за 4 пикселя.
    ...


def move_snake():
    # TODO(4.3): реализовать перемещение змейки на одну ячейку
    #  в заданном направлении.
    #  * Какие параметры будет принимать функция?
    #  * Из каких действий будет состоять перемещение змейки?
    ...


def get_snake_new_head():
    # TODO(4.4): реализовать функцию определения нового
    #  положения головы змейки.
    #  * Какие параметры будет принимать функция?
    #  * Что функция будет возвращать?
    ...


def snake_hit_edge():
    # TODO(5.2): функция возвращает True,
    #  если змейка пересекла одну из границ окна.
    ...


def snake_hit_apple():
    # TODO(6.2): функция возвращает True, если голова
    #  змейки находится в той же ячейке, что и яблоко.
    ...


def snake_grow():
    # TODO(6.3): предложите максимально простой
    #  способ увеличения длины змейки.
    ...


def new_apple():
    # TODO(6.4): функция возвращает случайную ячейку,
    #  в которой будет располагаться яблоко.
    #  Для генерации случайной координаты воспользуйтесь
    #  функцией random.randint(a, b)
    ...


def get_direction():
    # TODO(7.3): функция возвращает направление движения
    #  в зависимости от нажатой клавиши:
    #  * pygame.K_LEFT
    #  * pygame.K_RIGHT
    #  * pygame.K_UP
    #  * pygame.K_DOWN
    #  Если нажата клавиша противоположного направления движения,
    #  то не менять направление.
    ...

def snake_hit_self():
    # TODO(8.2): функция возвращает True, если голова змеи
    #  пересеклась хотя бы с одним блоком хвоста.
    ...


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
>>>>>>> 13f344a (git push)
