def triangle(a,b,c):
    return cross(b - a, c - a) / 2
def cos(a, b):
    return dot(a, b) / (abs(a) * abs(b))
def dot(a, b):
    return a.real * b.real + a.imag * b.imag
def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def solve(xyi, xy):
    # anti_clockwise_sort:sort(key=cos((1,0)(0,0)(xyk-xyi)),reverse=True)
    xy = sorted(xy, key=lambda a:(a.real - xyi.real) / abs(a - xyi), reverse=True)

    area = [[[(float('inf'),) for i in range(len(xy))] for j in range(len(xy))] for k in range(max(q) + 1)]
    # triangle
    for j in range(len(xy) - 1):
        for k in range(j + 1, len(xy)):
            area[3][j][k] = triangle(xyi, xy[j], xy[k]), (xyi, xy[j], xy[k])

    # square,pentagon,,,, 
    for i in range(4, max(q) + 1):
        for j in range(len(xy)):
            for k in range(j + 1, len(xy)):
                for s in range(k + 1, len(xy)):                                
                    if math.isinf(area[i - 1][j][k][0]):
                        continue                
                    if triangle(xy[j], xy[k], xy[s]) <= 0:
                        continue #skip not convex polygon
                    tmp = area[3][k][s][0] + area[i - 1][j][k][0]
                    if not math.isnan(area[i][k][s][0]) and area[i][k][s][0] < tmp:
                        continue
                    area[i][k][s] = tmp, area[i - 1][j][k][1] + (xy[s],)
                
    min_space = [(float('inf'),)] * (max(q) + 1)
    for i in range(3, max(q) + 1):
        min_space[i] = min([y for x in area[i] for y in x], key=operator.itemgetter(0))
    
    return min_space

import sys
import operator
import math

f = sys.stdin

xy =[[int(i) for i in f.readline().split()] for _ in range(int(f.readline()))]
q = [int(f.readline()) for _ in range(int(f.readline()))]

xy = [x + y * 1j for x, y in xy]
id = {xyi:i+1 for i, xyi in enumerate(xy)}

xy.sort(key=operator.attrgetter('imag', 'real'))

min_space = [(float('inf'),) for i in range(max(q) + 1)]
while 2 < len(xy):
    xyi = xy.pop(0)
    min_space = [min(i, j, key=operator.itemgetter(0)) for i,j in zip(min_space,solve(xyi, xy))]

for qi in q:
    if math.isinf(min_space[qi][0]):
        print('NA')
    else:
        print(*[id[i] for i in min_space[qi][1]])