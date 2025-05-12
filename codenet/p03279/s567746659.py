import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from bisect import bisect_left

MOD = 10**9 + 7

N,M = map(int,readline().split())
X = list(map(int,readline().split()))
Y = list(map(int,readline().split()))

L = []; R = []
for x in X:
    i = bisect_left(Y,x) # 右出口
    if i in [0,M]:
        continue
    y0,y1 = Y[i-1:i+1]
    L.append(y0-x); R.append(y1-x)

# 座圧
Rtoi = {x:i for i,x in enumerate(sorted(set(R)),1)}
R = [Rtoi[r] for r in R]

if len(R) == 0:
    print(1)
    exit()

"""
・計算方法
・これをやるために実際にはBITを使う
dp = [0] * (max(R)+1)
for _,r in sorted(set(zip(L,R)),reverse=True):
    dp[r] += 1 + sum(dp[1:r]) #これをやるために BIT で dp を持つ
answer=1+sum(dp)
print(answer)
"""

class BIT():
    def __init__(self, max_n):
        self.size = max_n + 1
        self.tree = [0] * self.size
        
    def get_sum(self,i):
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
for _,r in sorted(set(zip(L,R)),reverse=True):
    x = dp.get_sum(r-1) + 1; x %= MOD
    dp.add(r,x)
answer=1+dp.get_sum(max(R))
answer %= MOD
print(answer)