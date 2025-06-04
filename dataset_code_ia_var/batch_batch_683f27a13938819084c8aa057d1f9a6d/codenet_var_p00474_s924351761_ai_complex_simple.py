from functools import reduce
from operator import itemgetter
from itertools import accumulate, count, takewhile, chain
from collections import deque

def loadIcicle():
    def to_ints(s): return list(map(int, s))
    N, L = map(int, input().strip().split())
    icicles = reduce(lambda acc, _: acc + [int(input().strip())], range(N), [])
    return icicles, N, L

def calcDiff(icicles, N):
    # Compose a function creating the neighbour difference pattern
    neighbour = lambda arr, idx: ((arr[(idx+1)%N] if idx+1 < N else 0) - arr[idx],
                                  arr[idx] - (arr[idx-1] if idx > 0 else 0))
    sign = lambda x: (x > 0) - (x < 0)

    pairs = list(map(lambda idx: neighbour(icicles, idx), range(N)))
    # Compute sign differences in a "clever" way
    def combine(a):
        r, l = a
        return sign(sign(r) - sign(l))
    return list(map(combine, pairs))

icicles, N, L = loadIcicle()
diff_2times = calcDiff(icicles, N)

time = [-1]*N
peakX = list(filter(lambda i: diff_2times[i]==-1, range(N)))

for i in peakX:
    time[i] = L - icicles[i]

    markers = {'L': False, 'R': False}
    positions = {'L': i, 'R': i}

    for direction in ['L', 'R']:
        step = -1 if direction == 'L' else 1
        pos = positions[direction]
        marker = "isLocalMin" + direction
        while not markers[direction]:
            pos += step
            if pos < 0 or pos >= N:
                markers[direction] = True
                continue

            adj = [time[j] for j in [(pos-1), (pos+1)] if 0 <= j < N]
            fun = (lambda v: (L-icicles[pos]) + (v if adj == [] else max(adj)))
            nxt = fun(time[pos+(-step)] if time[pos] == -1 else max(adj))
            time[pos] = (L-icicles[pos]) + (time[pos-step] if time[pos] == -1 else max(adj))

            if diff_2times[pos] == 1:
                markers[direction] = True

print(reduce(lambda a, b: a if a > b else b, time))