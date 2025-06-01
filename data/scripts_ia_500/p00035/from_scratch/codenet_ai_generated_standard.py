def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

import sys
for line in sys.stdin:
    if not line.strip():
        continue
    data = list(map(float,line.strip().split(',')))
    A,B,C,D = data[0:2], data[2:4], data[4:6], data[6:8]
    points = [A,B,C,D]
    signs = []
    n = 4
    for i in range(n):
        o = points[i]
        a = points[(i+1)%n]
        b = points[(i+2)%n]
        cp = cross(o,a,b)
        signs.append(cp>0)
    if all(signs) or not any(signs):
        print("YES")
    else:
        print("NO")