class Animal:
    def sound(self):
        return "no Sound"


class Dog:
    def noflegs(self):
        return 4


dog = Dog()

print(dog.noflegs())
print(dog.sound())  # Error
