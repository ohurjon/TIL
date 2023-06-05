import struct

file = open('score.dat', 'rb')

file.seek(62, 0)

raw_data = file.read(62)

data = struct.unpack('>50s3i', raw_data)

print(data[0].decode().replace('\00', ""))
print(data[1:])
file.seek(0, 0)

raw_data = file.read(62)

data = struct.unpack('>50s3i', raw_data)

print(data[0].decode().replace('\00', ""))
print(data[1:])
file.close()
