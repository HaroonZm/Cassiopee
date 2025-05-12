import sys,queue,math,copy,itertools
from fractions import gcd
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
_LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]

N = int(input())
A = LI()+[-1]

ans = 0
l = 0
r = 0
xor = 0
s = 0

while r < N:

    if xor & A[r] == 0:
        xor ^= A[r]
        r += 1
        ans += (r - l)
    else:
        s = xor & A[r]
        while s:
            s -= s & A[l]
            xor ^= A[l]
            l += 1
#            if l == r : break
print (ans)