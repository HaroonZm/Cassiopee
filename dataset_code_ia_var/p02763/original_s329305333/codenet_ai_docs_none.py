import sys
def input():
    return sys.stdin.readline()[:-1]
INF = float("inf")
class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N+1)
    def add(self, x, a):
        while x <= self.N:
            self.bit[x] += a
            x += x & -x
    def sum(self, x):
        ret = 0
        while x != 0:
            ret += self.bit[x]
            x -= x & -x
        return ret
N = int(input())
S = list(input())
Q = int(input())
bit = [BIT(N+1) for i in range(26)]
for i in range(N):
    bit[ord(S[i])-97].add(i+1, 1)
for i in range(Q):
    q, x, y = input().split()
    q = int(q)
    if q == 1:
        i = int(x)-1
        bit[ord(S[i])-97].add(i+1, -1)
        S[i] = y
        bit[ord(y)-97].add(i+1, 1)
    else:
        l, r, ans = int(x), int(y), 0
        for i in range(26):
            ans += (bit[i].sum(r)-bit[i].sum(l-1)) > 0
        print(ans)