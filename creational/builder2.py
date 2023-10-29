from abc import ABC, abstractmethod


class IBuilder(ABC):
    @staticmethod
    @abstractmethod
    def build_wall(): ...

    @staticmethod
    @abstractmethod
    def build_roof(): ...

    @staticmethod
    @abstractmethod
    def coloring_house(): ...

    @staticmethod
    @abstractmethod
    def light_installation(): ...

    @staticmethod
    @abstractmethod
    def get_result(): ...


class House:
    house = list()


class ConstructHouse(IBuilder):
    def __init__(self):
        self.house = House()

    def build_wall(self):
        self.house.house.append('add wall')
        return self

    def build_roof(self):
        self.house.house.append('add roof')
        return self

    def coloring_house(self):
        self.house.house.append('add color')
        return self

    def light_installation(self):
        self.house.house.append('add light')
        return self

    def get_result(self):
        return self.house


class HouseDirector:
    @staticmethod
    def construct():
        return ConstructHouse().build_wall().build_roof().coloring_house().light_installation().get_result()


if __name__ == '__main__':
    h = HouseDirector()
    print(h.construct().house)

