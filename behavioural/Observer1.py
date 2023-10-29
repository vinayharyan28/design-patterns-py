from abc import ABC, abstractmethod


class IObservable(ABC):
    @staticmethod
    @abstractmethod
    def subscribe(observer): ...

    @staticmethod
    @abstractmethod
    def unsubscribe(observer): ...

    @staticmethod
    @abstractmethod
    def notify(message): ...


class IObserver(ABC):
    @staticmethod
    @abstractmethod
    def notify(message): ...


class Subject(IObservable):
    def __init__(self):
        self.observers = set()

    def subscribe(self, observer):
        self.observers.add(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observ in self.observers:
            observ.notify(message)


class Observer(IObserver):
    def __init__(self, observer):
        observer.subscribe(self)

    def notify(self, args):
        print(f'Id: {id(self)}: ', args)


subject = Subject()

observer1 = Observer(subject)
observer2 = Observer(subject)

subject.notify('Hi all')

subject.unsubscribe(observer1)

subject.notify('by all')



