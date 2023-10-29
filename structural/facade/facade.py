class SubSystemClassA:
    @staticmethod
    def method():
        return 'A'


class SubSystemClassB:
    @staticmethod
    def method(string):
        return string


class SubSystemClassC:
    @staticmethod
    def method(var_dict):
        return var_dict


class Facade:
    @staticmethod
    def sub_system_class_a():
        return SubSystemClassA.method()

    @staticmethod
    def sub_system_class_b(string):
        return SubSystemClassB.method(string)

    @staticmethod
    def sub_system_class_c(bio):
        return SubSystemClassC.method(bio)


f = Facade()
print(f.sub_system_class_a())
print(f.sub_system_class_b('Vinay'))
print(f.sub_system_class_c({'name': 'Vinay', 'last_name': 'Haryan'}))












