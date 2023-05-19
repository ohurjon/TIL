class Animal:
    def __init__(self):
        self.sound_str = 'No Sound'

    def sound(self):
        return self.sound_str


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.sound_str = "Bowwow"


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.sound_str = "Mew"


cat = Cat()
dog = Dog()

print(cat.sound())
print(dog.sound())
