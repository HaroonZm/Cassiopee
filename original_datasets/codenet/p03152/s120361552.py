import sys
input = sys.stdin.readline
from collections import *

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sa = set(A)
sb = set(B)
row, col = 0, 0
ans = 1
MOD = 10**9+7

for i in range(N*M, 0, -1):
    if (i in sa) and (i in sb):
        row += 1
        col += 1
    elif (i not in sa) and (i in sb):
        ans *= row
        col += 1
    elif (i in sa) and (i not in sb):
        ans *= col
        row += 1
    else:
        ans *= row*col-(N*M-i)
    
    ans %= MOD

print(ans)