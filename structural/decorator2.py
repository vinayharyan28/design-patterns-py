from abc import ABC, abstractmethod


class IValue(ABC):
    @abstractmethod
    def __str__(self): ...


class Value(IValue):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Add(IValue):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.add = self.value1.value + self.value2.value

    def __str__(self):
        return str(self.add)


class Sub(IValue):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.sub = self.value2.value - self.value1.value

    def __str__(self):
        return str(self.sub)


if __name__ == '__main__':
    v1 = Value(1)
    v2 = Value(2)
    v3 = Value(3)

    print(Add(v1, v2))
    print(Sub(v1, v2))

