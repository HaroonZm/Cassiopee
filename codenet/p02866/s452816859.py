from collections import Counter
MOD = 998244353

N = int(input())
D = list(map(int, input().split()))
C = Counter(D)
if D[0] != 0 or C[0] != 1:
    print(0)
    exit()
ans = 1
for i in range(1, max(D)+1):
    if C[i] == 0:
        ans = 0
        break
    else:
        ans *= pow(C[i-1], C[i], MOD)
        ans %= MOD
print(ans)

# import sys
# sys.setrecursionlimit(10000000)
# def input():
#     return sys.stdin.readline()[:-1]
# from bisect import *
# from collections import *
# from heapq import *
# import functools
# import itertools
# import math
# INF = float('inf')
# # MOD = 10**9+7
# MOD = 998244353
#
# N = int(input())
# D = list(map(int, input().split()))
# if D[0] != 0:
#     print(0)
# C = Counter(D)
# ans = 1
# for i in range(1, max(D)+1):
#     if C[i] == 0:
#         ans = 0
#         break
#     else:
#         ans *= pow(C[i-1], C[i], MOD)
#         ans %= MOD
# print(ans)