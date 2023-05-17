class LectureScore:
    RANGE_OF_SCORE = (0, 100)
    MIN = RANGE_OF_SCORE[0]
    MAX = RANGE_OF_SCORE[1]

    def __init__(self):
        self.lectures = {}

    def contains_lecture(self, lec_name):
        return lec_name in self.lectures.keys()

    def add_lecture(self, lec_name):
        self.lectures[lec_name] = []

    def get_lecture_scores(self, lec_name):
        if self.contains_lecture(lec_name):
            return self.lectures[lec_name]
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
        for scores in self.lectures.values():
            for score in scores:
                sumScore += score
        return sumScore





