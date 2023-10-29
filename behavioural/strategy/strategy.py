from abc import ABC, abstractmethod


class IStrategy(ABC):
    @abstractmethod
    def method(self): ...


class Strategy1(IStrategy):
    def method(self):
        print('Strategy1 called.')


class Strategy2(IStrategy):
    def method(self):
        print('Strategy2 called.')


class Strategy3(IStrategy):
    def method(self):
        print('Strategy3 called.')


class Context:
    @staticmethod
    def request(strategy):
        return strategy()


if __name__ == '__main__':
    context = Context()
    context.request(Strategy1).method()
    context.request(Strategy2).method()
    context.request(Strategy3).method()
