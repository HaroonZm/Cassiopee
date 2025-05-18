import sys, math
def input():
    return sys.stdin.readline()[:-1]
from itertools import permutations, combinations
from collections import defaultdict

sys.setrecursionlimit(10**7)
A, B, K = map(int, input().split())

if K <= A:
    print(A-K, B)
else:
    print(0, max(0, B-(K-A)))