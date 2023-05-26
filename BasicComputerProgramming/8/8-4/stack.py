class Stack:
    def __init__(self):
        self.__data = []

    def push(self, ele):
        self.__data.append(ele)

    def pop(self):
        try:
            return self.__data.pop()
        except IndexError:
            return None

    def getsize(self):
        return len(self.__data)
