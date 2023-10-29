from abc import ABC, abstractmethod


class Shape(ABC):
    @staticmethod
    @abstractmethod
    def draw(): ...


class ShapeFactory(ABC):
    @staticmethod
    @abstractmethod
    def crete_shape(): ...


class Circle(Shape):
    @staticmethod
    def draw():
        print('drawing circle...')


class Square(Shape):
    @staticmethod
    def draw():
        print('drawing square...')


class CircleFactory(ShapeFactory):
    @staticmethod
    def crete_shape():
        return Circle()


class SquareFactory(ShapeFactory):
    @staticmethod
    def crete_shape():
        return Square()


if __name__ == '__main__':
    circle_factory = CircleFactory()
    circle = circle_factory.crete_shape()
    circle.draw()

    square_factory = SquareFactory()
    square = square_factory.crete_shape()
    square.draw()
