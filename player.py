from settings import *
import pygame as pg
import math  # библиотека математики


class Player:
    """
    Основной класс игрока.
    :return:
    """

    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        """
        Метод перемещения игрока.
        Отрабатываем связь игрока с кнопками.
        :return:
        """
        sin_a = math.sin(self.angle)  # угол направления по синусу
        cos_a = math.cos(self.angle)  # угол направления по косинусу
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time  # обращаемся к переменной скорости игрока
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        # получаем информацию о нажатых клавишах
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:  # если нажата кнопка W
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:  # если нажата кнопка S
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:  # если нажата кнопка A
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:  # если нажата кнопка D
            dx += -speed_sin
            dy += speed_cos

        self.x += dx  # применяем наш dx
        self.y += dy  # применяем наш dy

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def draw(self):
        """
        Тестовый метод модели нашего игрока.
        :return:
        """
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                     (self.x * 100 + WIDTH * math.cos(self.angle),
                      self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def update(self):
        """
        Метод обновления.
        :return:
        """
        self.movement()

    # удобства создадим свойства
    @property
    def pos(self):
        """
        Свойство возвращает координаты игрока.
        :return:
        """
        return self.x, self.y

    @property
    def map_pos(self):
        """
        Свойство возвращает целочисленные координаты игрока.
        :return:
        """
        return int(self.x), int(self.y)
