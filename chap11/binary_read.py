import struct

struct_fmt = '16s2fi'
struct_len = struct.calcsize(struct_fmt)

cities = list()
with open('cities.dat', 'rb') as file:
    while True:
        buffer = file.read(struct_len)
        if not buffer:
            break
        city = struct.unpack(struct_fmt, buffer)
        cities.append(city)

    for city in cities:
        name = city[0].decode(encoding='utf=8').replace('\x00', '')
        print('City:{}, Lat/Long:{}/{}, Population:{}'.format(name, city[1], city[2], city[3]))