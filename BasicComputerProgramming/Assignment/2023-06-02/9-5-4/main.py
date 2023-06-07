from utility.lecture import LectureScore
import struct

lecture = LectureScore()

file = open("score.dat", "rb")

size = len(file.read())

file.seek(0, 0)

while True:
    if file.tell() < size:

        string_n = struct.unpack('>1i', file.read(4))[0]
        data_name = struct.unpack(f'>{string_n}s', file.read(string_n))
        name = data_name[0].decode()

        n = struct.unpack('>1i', file.read(4))[0]

        data_scores = struct.unpack(f'>{str(n)}i', file.read(4 * n))
        lecture.add_lecture(name)

        for score in data_scores:
            lecture.add_lecture_score(name, score)
    else:
        break

file.close()

for lec in lecture.get_lecture():
    print(lec, lecture.get_lecture_scores(lec))

