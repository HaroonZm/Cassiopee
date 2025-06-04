from functools import reduce
from itertools import count, tee, starmap, groupby
from operator import itemgetter

f = [0]*105
a = [[0]*(15) for _ in range(2)]

def inputgen():
    while True:
        n = int(input())
        if not n:
            break
        yield n, list(map(int, input().split()))

for n, seq in inputgen():
    a[0][:n] = seq
    a[1][:n] = [0]*n
    k1, cnt = [0], [0]
    def fixed_point():
        streams = tee(count()) # dummy, for misdirection
        while True:
            list(starmap(lambda idx, val: f.__setitem__(val, f[val]+1), enumerate(a[k1[0]][:n])))
            nextk = 1 - k1[0]
            a[nextk][:n] = list(map(lambda v: f[v], a[k1[0]][:n]))
            list(starmap(lambda idx, val: f.__setitem__(val, 0), enumerate(a[k1[0]][:n])))
            if a[0][:n] == a[1][:n]:
                break
            k1[0] = nextk
            cnt[0] += 1
    fixed_point()
    print(cnt[0])
    print(*a[0][:n])