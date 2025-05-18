import bisect
MOD = 10**9 + 7
 
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
  
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
  
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
 
n, k = [int(item) for item in input().split()]
a = [int(item) for item in input().split()]
bit = Bit(2010 * 2)
ans = 0
 
for i, p in enumerate(a):
    bit.add(p, 1)
    ans += i + 1 - bit.sum(p)
 
a.sort()
big = 0
for item in a:
    big += n - bisect.bisect_right(a, item)
 
times = (k * (k - 1) // 2) % MOD
ans2 = (ans * k) % MOD + (big * times) % MOD
ans2 %= MOD
print(ans2)