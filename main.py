# основной класс игры

import sys
from settings import *  # обращаемся к нашему файлу settings.py
from map import *  # обращаемся к нашему файлу map.py
from player import *  # обращаемся к нашему файлу player.py

class Game:
    """
    Основной класс игры DoomPY.
    :return:
    """
    def __init__(self):  # метод инициализации объектов
        pg.init()  # инициализируем сюда методы pygame
        self.screen = pg.display.set_mode(RES)  # обратимся к переменной из settings.py
        self.clock = pg.time.Clock()  # вызываем часы
        self.delta_time = 1  # чтобы скорость игрока не зависела от скорости чистоты кадров
        self.new_game()

    def new_game(self):
        """
        Метод новой_игры DoomPY.
        :return:
        """
        self.map = Map(self)  # вызываем карту
        self.player = Player(self)  # обратимся к классу Player

    def update(self):
        """
        Метод обновления экрана.
        Отображаем в нём текущее количество кадров.
        :return:
        """
        self.player.update()  # обратимся к классу Player
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)  # обратимся к переменной из settings.py
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        """
        Метод покраски нашего экрана.
        :return:
        """
        self.screen.fill('black')  # черный экран
        self.map.draw()
        self.player.draw()  # обратимся к классу Player

    def check_events(self):
        """
        Метод проверки событий методом перебора. Здесь будем проверять на выход или
        закрытие окна. И если такие события происходит то мы будем выходить.
        :return:
        """
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        """
        Метод запуска, в котором через цикл While будут
        запускаться методы, update и draw.
        :return:
        """
        while True:  # основной цикл
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':  # вызываем экземпляр нашего класса
    game = Game()
    game.run()
