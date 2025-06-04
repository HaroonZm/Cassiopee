from itertools import islice, tee, cycle, count, takewhile
from functools import reduce
from operator import itemgetter

def frange():
    while True:
        v = input()
        try:
            yield int(v)
        except:
            continue

g = frange()
for cid in count(1):
    n = next(g)
    if not n: break
    pts = list(map(lambda l: tuple(map(int, input().split())), range(n)))
    xy = list(zip(*tee(cycle(pts),2)))
    vs = zip(pts, islice(cycle(pts),1,None))
    area = -0.5 * reduce(lambda acc, x: acc + (x[0][0]-x[1][0])*(x[0][1]+x[1][1]), vs, 0)
    print(cid, area)
    _ = input()