"""Вариант №5 работы ОП6 """


class Point:
    """Класс инициализирует точку"""

    def __init__(self, dot_x, dot_y):
        """
        Инициализирует объект класса
        :param dot_x: float
        :param dot_y: float
        """
        self.dot_x = float(dot_x)
        self.dot_y = float(dot_y)
        self.container = (dot_x, dot_y)

    def __str__(self):
        """
        Возвращает строковое представление экземпляра класса
        :return:
        """
        return f'({self.dot_x},{self.dot_y})'

    def __getattr__(self, item):
        """
        Метод проверки на наличие аттрибута
        :param item:
        """
        if item not in self.__dict__:
            raise KeyError
        return self.item


class PointContainer:
    """
    Класс создаёт контейнер, который будет хранить точки
    """
    point_container = []

    @classmethod
    def add_point(cls, point):
        """
        Добавление точки в контейнер
        :param point:
        """
        cls.point_container.append((point.dot_x, point.dot_y))

    def __getattr__(self, item):
        """
        Метод проверки на наличие аттрибута
        :param item:
        """
        if item not in self.__dict__:
            return 'Такого аттрибута не существует'
        return self.item


class Limit:
    """Класс создаёт линейное ограничение"""

    def __init__(self):
        """Функция инициализирует класс"""
        try:
            print('Задайте ограничение, введя x1, y1, x2, y2')
            self.dot_x1 = float(input('Введите первое значение по dot_x (x1): '))
            self.dot_y1 = float(input('Введите первое значение по y (y1): '))
            self.dot_x2 = float(input('Введите второе значение по dot_x (x2): '))
            self.dot_y2 = float(input('Введите второе значение по y (y2): '))
        except ValueError:
            print('Пожалуйста, введите корректные данные!')
            print('Задайте ограничение, введя x1, y1, x2, y2')
            self.dot_x1 = float(input('Введите первое значение по dot_x (x1): '))
            self.dot_y1 = float(input('Введите первое значение по y (y1): '))
            self.dot_x2 = float(input('Введите второе значение по x (x2): '))
            self.dot_y2 = float(input('Введите второе значение по y (y2): '))
        # print(type(self.dot_x1))
        # print(type(self.dot_y1))
        # print(type(self.dot_x2))
        # print(type(self.dot_y2))
        if (self.dot_x1 == self.dot_x2) and (self.dot_y1 == self.dot_y2):
            print('Точки не должны совпадать')
            try:
                print('Задайте ограничение, введя x1, y1, x2, y2')
                self.dot_x1 = float(input('Введите первое значение по x (x1): '))
                self.dot_y1 = float(input('Введите первое значение по y (y1): '))
                self.dot_x2 = float(input('Введите второе значение по x (x2): '))
                self.dot_y2 = float(input('Введите второе значение по y (y2): '))
            except ValueError:
                print('Пожалуйста, введите корректные данные!')
                print('Задайте ограничение, введя x1, y1, x2, y2')
                self.dot_x1 = float(input('Введите первое значение по x (x1): '))
                self.dot_y1 = float(input('Введите первое значение по y (y1): '))
                self.dot_x2 = float(input('Введите второе значение по x (x2): '))
                self.dot_y2 = float(input('Введите второе значение по y (y2): '))

    def check_point(self, point):
        """
        Функция проверяет точку на принадлежность точки к линейному ограничению
        :param point:
        :return:
        """
        print(type(point.dot_x))
        print(type(point.dot_y))
        if ((self.dot_x1 <= point.dot_x <= self.dot_x2) and
                (self.dot_y1 <= point.dot_y <= self.dot_y2)):
            return True
        return False

    # def __getattr__(self, item):
    #     """
    #     Метод проверки на наличие аттрибута
    #     :param item:
    #     """
    #     if item not in self.__dict__:
    #         raise KeyError
    #     return self.item


class LimitConfirmed:
    """Класс сохраняет в контейнер только точки, что подходят под ограничение"""
    confirm = []

    @classmethod
    def checker(cls, container, checker):
        """Метод проверяет точки из контейнера на принадлежность к ограничению"""
        for dot_x, dot_y in container.point_container:
            if checker.check_point(Point(dot_x, dot_y)):
                cls.confirm.append((dot_x, dot_y))

        def pretty_output(arr):
            pretty = 'Данные точки входят в заданное ограничение: '
            for item in arr:
                pretty += str(item) + ', '
            return pretty[:-2]

        return pretty_output(cls.confirm)

    # def __getattr__(self, item):
    #     """
    #     Метод проверки на наличие аттрибута
    #     :param item:
    #     """
    #     if item not in self.__dict__:
    #         return 'Такого аттрибута не существует'
    #     return self.item
