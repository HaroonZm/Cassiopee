from collections import Counter,deque
from sys import stdin,setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

n, t = map(int, input().split())
ac = [0] * (t + 1)
i = 0
while i < n:
    l, r = map(int, input().split())
    ac[l] += 1
    ac[r] -= 1
    i += 1
j = 1
while j <= t:
    ac[j] += ac[j - 1]
    j += 1
m = ac[0]
k = 1
while k <= t:
    if ac[k] > m:
        m = ac[k]
    k += 1
print(m)