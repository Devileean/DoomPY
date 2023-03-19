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
        :return:
        """
        sin_a = math.sin(self.angle)  # угол направления по синусу
        cos_a = math.cos(self.angle)  # угол направления по косинусу
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time  # обращаемся к переменной скорости игрока
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

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
