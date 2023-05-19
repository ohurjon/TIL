class BaseClass:
    def __init__(self):
        print("Base Class")

class DerivedClass(BaseClass):
    def __init__(self):
        print('Derived Class')

d = DerivedClass()
b= BaseClass()