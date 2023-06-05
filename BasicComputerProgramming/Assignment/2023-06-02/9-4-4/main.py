import struct

file = open('float10.data', 'rb')

data = struct.unpack('>10f', file.read())

file.close()

print(data)
