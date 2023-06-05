from utility.lecture import LectureScore
import struct

lecture_data = {
    "korean": [90, 95, 88],
    "english": [88, 91, 93]
}

lecture = LectureScore()

for lecture_name in lecture_data.keys():
    lecture.add_lecture(lecture_name)
    for score in lecture_data[lecture_name]:
        lecture.add_lecture_score(lecture_name, score)

file = open("score.dat", "wb")

data = bytes()

for lec in lecture.get_lecture():
    data += struct.pack('>50s3i', lec.encode(), *lecture.get_lecture_scores(lec))


file.write(data)

print(len(data))
file.close()
