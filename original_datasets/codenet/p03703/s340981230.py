from itertools import accumulate

class BIT:
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
            
def compress(arr):
    a = sorted([(v,k) for k,v in enumerate(arr)])
    return [k+1 for v,k in a]

n,k = map(int, input().split())
a = [int(input())-k for i in range(n)]
cumsum = [0] + list(accumulate(a))
comp = compress(cumsum)
bit = BIT(n+1)
ans = n * (n+1) // 2
for k,v in enumerate(comp):
  bit.add(v,1)
  ans -= k+1-bit.sum(v)
print(ans)