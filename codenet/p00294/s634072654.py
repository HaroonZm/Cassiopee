import itertools as ite
import math

INF = 10 ** 18

N, M, p = map(int, raw_input().split())
ls = []
for i in range(M):
    ls.append((input() - p) % N)
ls = sorted(ls)
ans = min(ls[-1], N - ls[0])
for i in range(M - 1):
    len1 = ls[i]
    len2 = N - ls[i + 1]
    ans = min(ans, len1 * 2 + len2, len2 * 2 + len1)
print ans * 100