class LectureScore:
    lectures = {}

    def getLectureScore(self, name):
        pass

    def getScore(self):
        pass

    def addScore(self, name, score):
        self.lectures[name] = score

    def modifyScore(self, name, score):
        self.lectures[name] = score

    def getTotalScore(self):
        pass


score = LectureScore()

print(type(score))
