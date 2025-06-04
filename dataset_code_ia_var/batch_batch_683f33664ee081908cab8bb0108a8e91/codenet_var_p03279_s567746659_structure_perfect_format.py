import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from bisect import bisect_left

MOD = 10**9 + 7

N, M = map(int, readline().split())
X = list(map(int, readline().split()))
Y = list(map(int, readline().split()))

L = []
R = []
for x in X:
    i = bisect_left(Y, x)
    if i in [0, M]:
        continue
    y0, y1 = Y[i - 1:i + 1]
    L.append(y0 - x)
    R.append(y1 - x)

Rtoi = {x: i for i, x in enumerate(sorted(set(R)), 1)}
R = [Rtoi[r] for r in R]

if len(R) == 0:
    print(1)
    exit()

class BIT():
    def __init__(self, max_n):
        self.size = max_n + 1
        self.tree = [0] * self.size

    def get_sum(self, i):
        s = 0
        while i:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < self.size:
            self.tree[i] += x
            i += i & -i

dp = BIT(max_n=max(R))
for _, r in sorted(set(zip(L, R)), reverse=True):
    x = dp.get_sum(r - 1) + 1
    x %= MOD
    dp.add(r, x)
answer = 1 + dp.get_sum(max(R))
answer %= MOD
print(answer)