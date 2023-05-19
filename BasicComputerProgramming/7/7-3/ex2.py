class App:
    def __init__(self):
        self.__flag = True
    def flag_set(self, value):
        if isinstance(value, bool):
            self.__flag = value
        else:
            raise ValueError
    def flag_get(self):
        return self.__flag


app = App()
print(app.__flag) #Error : Private Variable Access
app.flag = "good morning"

print(app.__flag)
