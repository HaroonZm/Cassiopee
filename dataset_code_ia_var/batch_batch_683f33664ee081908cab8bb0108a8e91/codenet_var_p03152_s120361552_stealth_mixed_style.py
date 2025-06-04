from sys import stdin
from collections import Counter

def GetInput():
    return map(int, stdin.readline().split())

N_M = GetInput()
_ = lambda: list(map(int, stdin.readline().split()))
a = set(_())
b = set(_())
R, C, ret = 0, 0, 1
M = 10**9+7

for k in range(N_M[0]*N_M[1], 0, -1):
    if k in a:
        if k in b:
            R += 1
            C += 1
        else:
            ret = (ret * C) % M
            R += 1
    elif k in b:
        ret *= R
        ret %= M
        C = C + 1
    else:
        from math import prod
        temp = R * C - (N_M[0]*N_M[1] - k)
        ret = ret * temp
        ret = ret % M

print(ret)