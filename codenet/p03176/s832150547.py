class Bit:
    """1-indexed"""

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def max(self, i):
        m = 0
        while i > 0:
            m = max(m, self.tree[i])
            i -= i & -i
        return m

    def update(self, i, x):
        while i <= self.size:
            self.tree[i] = max(x, self.tree[i])
            i += i & -i

N = int(input())
H = tuple(map(int, input().split()))
A = tuple(map(int, input().split()))

S = sorted([(h, i) for i, h in enumerate(H)])

dp = Bit(N)
for h, i in S:
    dp.update(i + 1, dp.max(i) + A[i])
print(dp.max(N))