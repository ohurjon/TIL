class LectureScore:
    RANGE_OF_SCORE = (0, 100)
    RANGE_MIN = RANGE_OF_SCORE[0]
    RANGE_MAX = RANGE_OF_SCORE[1]

    def __init__(self):
        self.lectures = {}

    def add_lecture(self, lec_name):
        if lec_name not in self.lectures.keys():
            self.lectures[lec_name] = []

    def get_lecture_scores(self, lec_name):
        return self.lectures[lec_name]

    def add_lecture_score(self, lec_name, score):
        if lec_name in self.lectures.keys():
            if LectureScore.RANGE_MIN <= score <= LectureScore.RANGE_MIN:
                self.lectures[lec_name].append(score)


lee_lecture = LectureScore()
lee_lecture.add_lecture('korean')
lee_lecture.add_lecture_score('korean', 95)
print(lee_lecture.get_lecture_scores('korean'))
