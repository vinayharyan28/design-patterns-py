from abc import ABC, abstractmethod


class IInterpreter(ABC):
    @abstractmethod
    def interpret(self): ...


class Value(IInterpreter):
    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

    def __repr__(self):
        print('value ', self.value)
        return str(self.value)


class Add(IInterpreter):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

    def __repr__(self):
        print(f'({self.left} Add {self.right})')
        return f'({self.left} Add {self.right})'


class Subtract(IInterpreter):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        print(f'({self.left} Subtract {self.right})')
        return f'({self.left} Subtract {self.right})'


class Multiply(IInterpreter):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()

    def __repr__(self):
        return f'({self.left} Multiply {self.right})'


class Divide(IInterpreter):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() // self.right.interpret()

    def __repr__(self):
        return f'({self.left} Divide {self.right})'


class Modulo(IInterpreter):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() % self.right.interpret()

    def __repr__(self):
        return f'({self.left} Modulo {self.right})'


if __name__ == '__main__':
    expression = []
    expression_string = "5 + 4 - 3 + 7 - 2"
    token = expression_string.split(' ')
    print(token)

    expression.append(Add(Value(token[0]), Value(token[2])))
    expression.append(Subtract(expression[0], Value(token[4])))
    expression.append(Add(expression[1], Value(token[6])))
    expression.append(Subtract(expression[2], Value(token[8])))

    print('expression: ', expression[-1])
    print('expression output: ', expression[-1].interpret())































