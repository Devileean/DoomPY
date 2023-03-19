#  здесь будет рисоваться наша карта
import pygame as pg

_ = False  # двумерный массив (мини карта), где цифры это стены, а подчёркивания пустота
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Map:
    """
    Класс карты игры DoomPY.
    :return:
    """
    def __init__(self, gane):
        self.gane = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        """
        Метод где перебираем наши числовые значения нашего
        массива mini_map.
        :return:
        """
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        """
        Метод вывода нашей mini_map на экран.
        Где будет рисовать наши элементы в виде не заполненного квадрата.
        :return:
        """
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]