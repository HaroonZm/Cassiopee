import sys
import copy
from collections import deque
stdin = sys.stdin

mod = 10**9+7

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n = ni()
a_list = na()

c = {abs((n-1-i)-i): 0 for i in range(n//2 + 1)}

for a in a_list:
    if a not in c or c[a]==2:
        print(0)
        exit(0)
    c[a] += 1

cnt = 1
for k,v in c.items():
    if v==2 or k==0:
        cnt *= v
        cnt %= mod
    else:
        print(0)
        exit(0)

print(cnt)