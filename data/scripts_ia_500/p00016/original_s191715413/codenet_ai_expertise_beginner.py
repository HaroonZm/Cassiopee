import math
nowx = 0
nowy = 0
nowa = 90
while True:
    line = raw_input()
    parts = line.split(',')
    d = int(parts[0])
    a = int(parts[1])
    if d == 0 and a == 0:
        print int(nowx)
        print int(nowy)
        break
    else:
        angle_in_radians = nowa * math.pi / 180.0
        nowx = nowx + math.cos(angle_in_radians) * d
        nowy = nowy + math.sin(angle_in_radians) * d
        nowa = nowa - a