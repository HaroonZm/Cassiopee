import sys
import bisect

input = sys.stdin.readline

n = int(input())
vert = []
horiz = []
ys = set()

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        vert.append((x1, y1, y2))
        ys.add(y1)
        ys.add(y2)
    else:
        if x1 > x2:
            x1, x2 = x2, x1
        horiz.append((y1, x1, x2))
        ys.add(y1)

ys = sorted(ys)
coord_index = {y:i+1 for i,y in enumerate(ys)}

events = []
for y, x1, x2 in horiz:
    events.append((x1, 0, coord_index[y]))  # horizontale début
    events.append((x2, 2, coord_index[y]))  # horizontale fin
for x, y1, y2 in vert:
    events.append((x, 1, coord_index[y1], coord_index[y2]))  # verticale

events.sort(key=lambda e: (e[0], e[1]))

BIT = [0]*(len(ys)+2)

def add(i, v):
    while i < len(BIT):
        BIT[i] += v
        i += i & -i

def query(i):
    s = 0
    while i > 0:
        s += BIT[i]
        i -= i & -i
    return s

res = 0
for e in events:
    if e[1] == 0:     # horizontale debut
        add(e[2], 1)
    elif e[1] == 2:   # horizontale fin
        add(e[2], -1)
    else:             # verticale
        res += query(e[4]) - query(e[3]-1)

print(res)