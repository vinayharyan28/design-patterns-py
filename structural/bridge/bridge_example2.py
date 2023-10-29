from abc import ABC, abstractmethod


class Run(ABC):
    @staticmethod
    @abstractmethod
    def running(): ...


class Compiler(ABC):
    @staticmethod
    @abstractmethod
    def compiling(): ...


class PythonCompiler(Compiler):
    @staticmethod
    def compiling():
        print('compiling .py file')


class JavaCompiler(Compiler):
    @staticmethod
    def compiling():
        print('compiling .java file')


class Python(Run):
    def __init__(self, compiler):
        self.py = compiler

    def running(self):
        self.py.compiling()
        print('run successfully')


class Java(Run):
    def __init__(self, compiler):
        self.java = compiler

    def running(self):
        self.java.compiling()
        print('run successfully')


py_file = PythonCompiler()
java_file = JavaCompiler()
python_run = Python(py_file)
java_run = Java(java_file)
python_run.running()
java_run.running()




















































































