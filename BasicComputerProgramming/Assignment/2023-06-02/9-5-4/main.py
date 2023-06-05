from utility.lecture import LectureScore
import struct

lecture = LectureScore()

file = open("score.dat", "rb")

size = len(file.read())

file.seek(0, 0)

while True:
    if file.tell() < size:
        byte_name = file.read(50)

        data_name = struct.unpack('>50s', byte_name)
        name = data_name[0].decode().replace('\00', "")

        byte_n = file.read(4)
        n = struct.unpack('>1i', byte_n)[0]

        byte_scores = file.read(4 * n)
        data_scores = struct.unpack('>' + str(n) + 'i', byte_scores)
        scores = data_scores

        print(scores)

        lecture.add_lecture(name)

        for score in scores:
            lecture.add_lecture_score(name, score)
    else:
        break

file.close()

for lec in lecture.get_lecture():
    print(lec, lecture.get_lecture_scores(lec))
