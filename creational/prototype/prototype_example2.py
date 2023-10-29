import copy


class ProtoType:
    def __init__(self):
        self.set_id = None
        self.pdf_file = None
        self.json_file = None
        self.text_file = None

    def clone(self):
        return copy.copy(self)


class Folder(ProtoType):
    def __init__(self):
        super().__init__()
        self.set_id = 1
        self.text_file = 'folder.txt'
        self.json_file = 'folder.json'
        self.pdf_file = 'folder.pdf'

    @staticmethod
    def folder():
        return 'inside folder'


class Folder1(ProtoType):
    def __init__(self):
        super().__init__()
        self.set_id = 2
        self.text_file = 'folder1.txt'
        self.pdf_file = 'folder1.pdf'
        self.json_file = 'folder1.json'

    @staticmethod
    def folder1():
        return 'inside folder 1'


class Folder2(ProtoType):
    def __init__(self):
        super().__init__()
        self.set_id = 3
        self.text_file = 'folder2.txt'
        self.pdf_file = 'folder2.pdf'
        self.json_file = 'folder2.json'

    @staticmethod
    def folder2():
        return 'inside folder 2'


class ProtoTypeDemo:
    CACHE = {}

    @staticmethod
    def load():
        ProtoTypeDemo.CACHE[1] = Folder()
        ProtoTypeDemo.CACHE[2] = Folder1()
        ProtoTypeDemo.CACHE[3] = Folder2()

    @staticmethod
    def get_prototype(get_id):
        return ProtoTypeDemo.CACHE[get_id].clone()


if __name__ == '__main__':
    prototype_demo = ProtoTypeDemo()
    prototype_demo.load()
    t1 = prototype_demo.get_prototype(3)
    print(t1.text_file)
