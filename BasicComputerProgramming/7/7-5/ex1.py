class D(object):
    def __init__(self):
        print("Class D")
        self.data =1

class B(D):
    def __init__(self):
        print("Class B")
        self.data = 2


class C(D):
    def __init__(self):
        print("Class C")
        self.data = 3
    def get(self):
        return self.data

    def calc(self, n):
        return self.data +n

class E(object):
    def __init__(self):
        print("Class E")
        self.data = 4

class A(B,C,E):
    def __init__(self):
        super(C,self).__init__()


obj = A()
print(obj.get())
print(obj.calc(9))

