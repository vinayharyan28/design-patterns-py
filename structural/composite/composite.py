from abc import ABC, abstractmethod


class IDeveloper(ABC):
    @staticmethod
    @abstractmethod
    def scope(): ...


class PythonDeveloper(IDeveloper):
    def __init__(self, scope, salary):
        self.scope = scope
        self.salary = salary

    def scope(self):
        print('course name: ', self.scope, 'course price: ', self.salary)


class PythonScope(IDeveloper):
    def __init__(self, developers):
        self.developer = developers

    def scope(self):
        for dev in self.developer:
            print('salary: ', dev.salary, 'scope: ', dev.scope)


py_data_science = PythonDeveloper('Data Science', 1000)
py_backend = PythonDeveloper('Backend', 1000)
py_data_analytics = PythonDeveloper('Data Analytics', 2000)
py_scope = PythonScope([py_backend, py_data_analytics, py_data_science])
py_scope.scope()
















































