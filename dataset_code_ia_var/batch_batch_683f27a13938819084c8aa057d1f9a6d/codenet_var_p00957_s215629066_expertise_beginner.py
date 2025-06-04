import sys

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

l, k = map(int, raw_input().split())

DP1 = [0] * 200
DP2 = [0] * 200
DP2[0] = 1

for i in range(1, l + 1):
    DP1[i] = DP2[i - 1]
    DP2[i] = DP1[i - 1]
    if i >= k:
        DP1[i] += DP2[i - k]

print sum(DP1)