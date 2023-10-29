class Courses:
    def accept(self, visitor):
        visitor.visit(self)

    def teaching(self, visitor):
        print(f'{self} taught by {visitor}')

    def studying(self, visitor):
        print(f'{self} study by {visitor}')

    def __str__(self):
        return self.__class__.__name__


class DSA(Courses): ...


class SDE(Courses): ...


class DataScience(Courses): ...


class Teacher:
    def visit(self, teach):
        return teach.teaching(self)

    def __str__(self):
        return self.__class__.__name__


class Student:
    def visit(self, study):
        return study.studying(self)

    def __str__(self):
        return self.__class__.__name__


dsa = DSA()
sde = SDE()
data_science = DataScience()

teacher = Teacher()
student = Student()

dsa.accept(teacher)
dsa.accept(student)

sde.accept(teacher)
sde.accept(student)
