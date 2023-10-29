from abc import ABC, abstractmethod


class IIterator(ABC):
    @staticmethod
    @abstractmethod
    def next(): ...

    @staticmethod
    @abstractmethod
    def has_next(): ...


class IAggregate(ABC):
    @staticmethod
    @abstractmethod
    def method(): ...


class Iterable(IIterator):
    def __init__(self, aggregator):
        self.index = 0
        self.aggregator = aggregator

    def next(self):
        if self.index < len(self.aggregator):
            aggregate = self.aggregator[self.index]
            self.index += 1
            return aggregate
        raise 'END of iteration.'

    def has_next(self):
        return self.index < len(self.aggregator)


class Aggregate(IAggregate):
    def method(self):
        print('Method invoked..')


if __name__ == '__main__':
    aggregators = [Aggregate(), Aggregate(), Aggregate(), Aggregate(), Aggregate()]
    iterator = Iterable(aggregators)
    while iterator.has_next():
        iterator.next().method()
