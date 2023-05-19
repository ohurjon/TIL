class Score:
    def __init__(self, point=0):
        print("init of Score")
        self.set(point)

    def set(self, point):
        self.point = point

    def get(self):
        return self.point


class IDScore(Score):
    def __init__(self, id, point=0):
        super().__init__(point)
        print("init of IDScore")
        self.id = id

    def getID(self):
        return self.id


mine = IDScore("G1234", 99)
print(mine.getID(), mine.get())
