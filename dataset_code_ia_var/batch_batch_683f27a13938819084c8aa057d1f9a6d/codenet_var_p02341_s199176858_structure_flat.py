import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9 + 7

n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])

if n <= k:
    ans = 1
else:
    ans = 0

print(ans)