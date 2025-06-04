from sys import stdin
from functools import reduce
from operator import mul

n = int(stdin.readline())
t = list(map(int, stdin.readline().split()))
a = list(map(int, stdin.readline().split()))
mod = 10 ** 9 + 7

if not any(ti == ai == t[-1] == a[0] for ti, ai in zip(t, a)):
    print(0)
else:
    ans = reduce(lambda acc, i: acc * min(t[i], a[i]) % mod if t[i-1]==t[i] and a[i]==a[i+1] else acc,
                 range(1, n-1), 1)
    print(ans)