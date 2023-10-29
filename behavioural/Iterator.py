"""The Iterator Pattern Concept"""


class NumberWheel:  # pylint: disable=too-few-public-methods
    """The concrete iterator (iterable)"""

    def __init__(self):
        self.index = 0

    def next(self):
        """Return a new number next in the wheel"""
        self.index = self.index + 1
        return self.index * 2 % 11


# The Client
number_wheel = NumberWheel()

for i in range(22):
    print(number_wheel.next(), end=", ")

print()
NAMES = ['SEAN', 'COSMO', 'EMMY']
for name in NAMES:
    print(name, end=", ")
print()

NAMES = ['SEAN', 'COSMO', 'EMMY']
iterator = iter(NAMES)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

print()

NAMES = ['SEAN', 'COSMO', 'EMMY']
iterator = NAMES.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())


class Doubler:
    count = 1

    @classmethod
    def next(cls):
        cls.count *= 2
        return cls.count

    __call__ = next


iterator = iter(Doubler(), 32)
print(list(iterator))
