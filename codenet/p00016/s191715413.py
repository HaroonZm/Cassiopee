import math
nowx = 0
nowy = 0
nowa = 90
while True:
    (d,a) = [int(i) for i in raw_input().split(',')]
    if(d == a == 0):
        print int(nowx)
        print int(nowy)
        break
    else:
        nowx += math.cos(nowa / 180.0 * math.pi) * d
        nowy += math.sin(nowa / 180.0 * math.pi) * d
        nowa -= a