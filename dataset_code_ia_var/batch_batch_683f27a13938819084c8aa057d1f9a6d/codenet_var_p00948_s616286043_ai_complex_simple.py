from functools import reduce
from itertools import starmap, tee, islice, chain
from operator import setitem, itemgetter

N, M = map(int, input().split())
XY = list(starmap(lambda x, y: (x, y), (map(int, input().split()) for _ in range(M))))
XY = sorted(XY, key=itemgetter(0))

minY = list(range(N))
maxY = list(range(N))

indices = ((y - 1, y) for _, y in XY)
def twist(z):
    a, b = z
    setitem(minY, b, minY[a])
    setitem(maxY, a, maxY[b])
    return z
list(map(twist, indices))

def diff(idx):
    return maxY[idx] - minY[idx] + 1
print(*map(diff, range(N)))