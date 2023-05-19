class Position:
    def __init__(self, x=0, y=0):
        self.set_position(x, y)

    def __str__(self):
        return f'(x, y) = ({self.__x}, {self.__y})'

    def set_position(self, x, y):
        if x >= 0 and y >= 0:
            self.__x = x
            self.__y = y

    def get_position(self):
        return (self.__x, self.__y)


center = Position(15, 20)
print(center.get_position())
print(center)
