import sys

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N,K=MAP()
AB=[LIST() for i in range(N)]

ans=0
for i in range(N):
    if K|AB[i][0]==K:
        ans+=AB[i][1]

Kb=format(K, 'b')
for i, b in enumerate(Kb):
    if b=='1':
        # あるビットが1だったら、そこは0にしてそこから先を全部1にする
        Kb2=Kb[:i]+'0'+'1'*(len(Kb[i:])-1)
        k=int(Kb2, 2)
        sm=0
        for i in range(N):
            if k|AB[i][0]==k:
                sm+=AB[i][1]
        ans=max(ans, sm)
print(ans)