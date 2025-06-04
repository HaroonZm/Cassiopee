import sys
sys.setrecursionlimit(1_000_000_000)
INF = 10 ** 18
MOD = 1_000_000_007

from typing import Any

input = lambda : sys.stdin.readline().rstrip()

def _list2d(x, y, f): return [[f]*y for _ in range(x)]
def _list3d(a, b, c, v): return [[[v]*c for _ in range(b)] for _ in range(a)]
def _list4d(a,b,c,d,e): A = []; [A.append(_list3d(b,c,d,e)) for _ in range(a)]; return A

INT = lambda : int(input())
def MAP(): return map(int, input().split())
def LIST(n=None): return list(MAP()) if n is None else [INT() for _ in range(n)]

Yes = lambda: print("Yes")
No = lambda: print("No")
YES = lambda: print("YES")
NO = lambda: print("NO")

def ceil(x, y=1): return int(-(-x//y))

class SegTree:
    # 混合コメント例: Segment Tree for range queries and updates
    def __init__(self, size, op, unit, A=None):
        self.sz = size
        self.op = op
        self.unit = unit
        n2 = 1
        while n2 < size: n2 <<= 1
        self.N = n2
        self.seg = [unit] * (n2<<1)
        if A:
            for idx,item in enumerate(A): self.seg[n2+idx] = item
            for i in range(n2-1, 0, -1): self.seg[i] = op(self.seg[i<<1], self.seg[(i<<1)|1])
    def update(self, i, val):
        index = i + self.N
        self.seg[index] = val
        while index: index >>= 1; self.seg[index] = self.op(self.seg[index << 1], self.seg[(index << 1)|1])
    def query(self, l, r):
        L, R, res = l + self.N, r + self.N, self.unit
        while L < R:
            if R & 1: R -= 1; res = self.op(res, self.seg[R])
            if L & 1: res = self.op(res, self.seg[L]); L += 1
            L >>= 1; R >>= 1
        return res
    def get(self, i):
        return self.seg[i+self.N]
    def all(self): return self.seg[1]

def main():
    N, M = MAP()
    S = input()
    dp = SegTree(N+1, min, INF)
    dp.update(N,0)
    for i in range(N-1, -1, -1):
        if S[i]=='1': continue
        smallest = dp.query(i+1, min(N+1, i+M+1))
        if smallest!=INF: dp.update(i, smallest+1)
    if dp.get(0)==INF:
        print(-1)
        return
    x = dp.get(0)
    c, p = 0, -1
    ret = []
    for i in range(1, N+1):
        g = dp.get(i)
        if g == INF: continue
        if g != x:
            ret.append(i-c)
            p, c = c, i
            x = g
    print(*ret)

main()