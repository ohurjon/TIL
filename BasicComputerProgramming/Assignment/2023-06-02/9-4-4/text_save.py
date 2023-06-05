import struct
import random

data = [random.random() for _ in range(10)]

bytes_data = struct.pack('>10f', *data)

print(data)

file = open('float10.data', "wb")

file.write(bytes_data)

file.close()
