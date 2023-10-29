class Colleague1:
    @staticmethod
    def method1():
        return 'College1 method called.'


class Colleague2:
    @staticmethod
    def method2():
        return 'College2 method called.'


class Mediator:
    def __init__(self):
        self.colleague1 = Colleague1()
        self.colleague2 = Colleague2()

    def method1(self):
        return self.colleague1.method1()

    def method2(self):
        return self.colleague2.method2()


if __name__ == '__main__':
    mediator = Mediator()
    print(mediator.method1())
    print(mediator.method2())


























