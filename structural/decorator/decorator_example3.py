from abc import ABCMeta, abstractmethod


class IValue(metaclass=ABCMeta):
    """Methods the component must implement"""

    @staticmethod
    @abstractmethod
    def __str__():
        """Override the object to return the value attribute by default"""


class Value(IValue):
    """A component that can be decorated or not"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Add(IValue):
    """A Decorator that Adds a number to a number"""

    def __init__(self, val1, val2):
        # val1 and val2 can be int or the custom Value
        # object that contains the `value` attribute
        val1 = getattr(val1, 'value')
        val2 = getattr(val2, 'value')
        self.value = val1 + val2

    def __str__(self):
        return str(self.value)


class Sub(IValue):
    """A Decorator that subtracts a number from a number"""

    def __init__(self, val1, val2):
        # val1 and val2 can be int or the custom Value
        # object that contains the `value` attribute
        val1 = getattr(val1, 'value')
        val2 = getattr(val2, 'value')
        print("val1 = ", val1)
        print("val2 = ", val2)
        self.value = val1 - val2

    def __str__(self):
        return str(self.value)


A = Value(1)
B = Value(2)
C = Value(5)

print(Sub(C, B))
print(Add(Sub(C, B), Sub(C, B)))

