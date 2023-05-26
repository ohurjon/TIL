from stack import Stack


class PostfixNotation:
    def __init__(self):
        self.__stack = Stack()
        self.__opr = {'+': self.__add, '*': self.__mul}

    def __add(self, n1, n2):
        return n1 + n2

    def __mul(self, n1, n2):
        return n1 * n2

    def calculate(self, expr):
        expr = expr.split()
        for item in expr:
            if item.isdigit():
                self.__stack.push(int(item))
            else:
                n2 = self.__stack.pop()
                n1 = self.__stack.pop()
                self.__stack.push(self.__opr[item](n1, n2))
        return self.__stack.pop()


postfix = PostfixNotation()
print(postfix.calculate('12 3 10 + *'))
