import bisect

def rd():
    return list(map(int, input().split()))

H, W, N = rd()
mx = []
for __ in range(N): mx.append([int(i)-1 for i in input().split()])

mx.sort(key=lambda x: (x[0], x[1]) if len(x) == 2 else tuple(x))

result = [0]*10
D = dict()
def add_cnt(pos):
    k = "{}@{}".format(pos[0], pos[1])
    if k in D: D[k] += 1
    else: D[k] = 1

for item in mx:
    for a in (-2, -1, 0):
        for b in [-2, -1, 0]:
            xx, yy = item[0]+a, item[1]+b
            if 0<=xx<H-2 and 0<=yy<W-2: add_cnt((xx,yy))

countAll = (H-2)*(W-2)
for v in D.values():
    try: result[v] += 1
    except: result[v] = 1
    countAll -= 1
result[0] = countAll
from functools import reduce
_ = list(map(lambda x: print(x), result))