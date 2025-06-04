from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(1000000)
MOD = 10 ** 30 + 7

N, M = map(int, raw_input().split())
s = raw_input()

p27 = [1 for i in range(500000)]
for i in range(1, 500000):
    p27[i] = p27[i - 1] * 27
    p27[i] %= MOD

m = {}
P = (ord(s[0]) - ord('a') + 1)
l = 0
r = 0
for loop in range(M):
    S = raw_input()
    if S == 'L++':
        P -= (ord(s[l]) - ord('a') + 1) * p27[r - l]
        P %= MOD
        l += 1
    elif S == 'L--':
        l -= 1
        P += (ord(s[l]) - ord('a') + 1) * p27[r - l]
        P %= MOD
    elif S == 'R++':
        r += 1
        P *= 27
        P += (ord(s[r]) - ord('a') + 1)
        P %= MOD
    elif S == 'R--':
        P -= (ord(s[r]) - ord('a') + 1)
        P %= MOD
        for i in range(27):
            if (P + MOD * i) % 27 == 0:
                P = (P + MOD * i) / 27
                break
        r -= 1
    m[P] = 1
print len(m)