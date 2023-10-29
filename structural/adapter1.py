from abc import ABC, abstractmethod


class IOne(ABC):
    @staticmethod
    @abstractmethod
    def development1(): ...


class ITwo(ABC):
    @staticmethod
    @abstractmethod
    def development2(): ...


class Product1(IOne):
    @staticmethod
    def development1():
        print('developing product one ... ')


class Product2(ITwo):
    @staticmethod
    def development2():
        print('developing product two ... ')


class Product1Adapter(ITwo):
    def __init__(self):
        self.product1 = Product1()

    def development2(self):
        self.product1.development1()


products = [Product2(), Product1Adapter()]
for i in products:
    i.development2()
