class App:
    def __init__(self):
        self.flag = True


app = App()
print(app.flag)
app.flag = "good morning"

print(app.flag)
