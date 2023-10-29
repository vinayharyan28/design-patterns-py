class Singleton:
    def __new__(cls):
        return cls

    @staticmethod
    def greeting():
        print('hellow singleton')


if __name__ == '__main__':
    s = Singleton()
    print(id(s))
    s2 = Singleton()
    print(id(s2))
