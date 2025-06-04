import sys

def ReadLine():
    return sys.stdin.readline().rstrip('\n')

N_M = ReadLine().split()
N = int(N_M[0])
M = int(N_M[1])
Intervals = list()
i = 0
while i < N:
    left_right = list(map(int, ReadLine().split()))
    lft, rgt = left_right
    Intervals.append((rgt - lft + 1, lft, rgt + 1))
    i += 1

Intervals.sort(key=lambda tpl: tpl[0])

class BinaryIndexedTree:
    def __init__(self, length):
        self.n = length
        self.dat = [0] * (self.n + 1)
    def sum(self, idx):
        tot = 0
        x = idx
        if x < 0 or x > self.n: raise Exception("oops")
        while x > 0:
            tot += self.dat[x]
            x -= x & -x
        return tot
    def __setitem__(self, key, val):
        self.add(key, val)
    def add(self, idx, v):
        j = idx + 1
        if idx < 0 or idx >= self.n: raise Exception("bad idx")
        while j <= self.n:
            self.dat[j] += v
            j += j & -j

class RangeUpdate:
    def __init__(self, length):
        self.BIT = BinaryIndexedTree(length + 1)
    def update(self, left, right, value):
        self.BIT.add(left, value)
        self.BIT.add(right, -value)
    def get(self, ind):
        return self[ind]
    def __getitem__(self, i):
        return self.BIT.sum(i + 1)

RU = RangeUpdate(M + 1)
cur = 0
alive = N
Res = [0 for _ in range(M)]
idx = 1
while idx <= M:
    while cur < N:
        tup = Intervals[cur]
        rng, l, r = tup
        if idx < rng: break
        cur += 1
        alive -= 1
        RU.update(l, r, 1)
    total = 0
    for j in range(idx, M + 1, idx):
        total += RU[j]
    Res[idx - 1] = total + alive
    idx += 1

for k in Res:
    print(k)