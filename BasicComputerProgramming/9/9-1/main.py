msg = "good_morning"
pi = 3.14

fd = open("datafile.txt", "w")

fd.write(msg)

fd.write(str(pi))

fd.close()

rfd = open('datafile.txt', 'r')

print(rfd.read())

rfd.close()
