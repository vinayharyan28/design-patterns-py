import random
from abc import ABC, abstractmethod


class IState(ABC):
    @abstractmethod
    def method(self): ...


class State1(IState):
    def method(self):
        return 'state1 executed.'


class State2(IState):
    def method(self):
        return 'state2 executed.'


class State3(IState):
    def method(self):
        return 'state3 executed.'


class Context:
    def __init__(self):
        self.states, self.handle = [State1(), State2(), State3()], None

    def request(self):
        self.handle = self.states[random.randint(0, 2)]
        return self.handle


context = Context()
print(context.request().method())
print(context.request().method())
print(context.request().method())
print(context.request().method())
print(context.request().method())
print(context.request().method())




















































































