class LectureScore:
    RANGE_OF_SCORE = (0, 100)
    MIN = RANGE_OF_SCORE[0]
    MAX = RANGE_OF_SCORE[1]

    def __init__(self):
        self.__lectures = {}

    def __str__(self):
        chars = ""
        for key in self.__lectures.keys():
            chars += key+" "
        return chars

    def contains_lecture(self, lec_name):
        return lec_name in self.__lectures.keys()

    def add_lecture(self, lec_name):
        self.__lectures[lec_name] = []

    def get_lecture_scores(self, lec_name):
        if self.contains_lecture(lec_name):
            return self.__lectures[lec_name]
        return []

    def get_lecture_sum(self, lec_name):
        sumScore = 0
        if self.contains_lecture(lec_name):
            for score in self.get_lecture_scores(lec_name):
                sumScore += score
        return sumScore

    def add_lecture_score(self, lec_name, score):
        if self.contains_lecture(lec_name):
            if LectureScore.MIN <= score <= LectureScore.MAX:
                self.get_lecture_scores(lec_name).append(score)

    def modify_lecture_score(self, lec_name, idx, score):
        if self.contains_lecture(lec_name):
            scores = self.get_lecture_scores(lec_name)
            if len(scores) > idx:
                scores[idx] = score

    def get_total_score(self):
        sumScore = 0
        for scores in self.__lectures.values():
            for score in scores:
                sumScore += score
        return sumScore

class IdentifyLectureScore(LectureScore):
    def __init__(self, *, id):
        super().__init__()
        self.__id = id

    def get_id(self):
        return self.__id
