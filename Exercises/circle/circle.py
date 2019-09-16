import math


class Circle:

    def __init__(self, radius=1):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self.radius = radius
        self.diameter = radius * 2
        self.__area = math.pi * (radius ** 2)

    def __str__(self):
        return f'Circle({int(self.__radius)})'

    def __repr__(self):
        return f'Circle({int(self.__radius)})'

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self.__radius = radius
        self.__diameter = radius * 2
        self.__area = math.pi * (radius ** 2)

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter):
        self.__diameter = diameter
        self.__radius = diameter / 2

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        raise AttributeError()



