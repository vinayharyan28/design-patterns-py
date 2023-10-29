from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @staticmethod
    @abstractmethod
    def step1(): ...

    @staticmethod  # hook optional for subclass
    def step2(): ...

    @staticmethod
    @abstractmethod
    def step3(): ...

    @classmethod
    def template_method(cls):
        cls.step1()
        cls.step2()
        cls.step3()


class ConcreateClassA(AbstractClass):
    @staticmethod
    def step1():
        print('step1 implement...')

    @staticmethod
    def step3():
        print('step3 implement...')


class ConcreateClassB(AbstractClass):
    @staticmethod
    def step1():
        print('step1 b implement...')

    @staticmethod
    def step3():
        print('step3 b implement...')

    @staticmethod
    def step2():
        print('step2 b overriding')


concreate_class_a = ConcreateClassA()
concreate_class_b = ConcreateClassB()
concreate_class_a.template_method()
concreate_class_b.template_method()


