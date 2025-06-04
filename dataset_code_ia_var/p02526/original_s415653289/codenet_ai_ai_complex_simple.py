from functools import reduce
from operator import and_
n = int(raw_input())
S = set(raw_input().split())
q = int(raw_input())
T = set(raw_input().split())
print reduce(lambda x, y: x + 1 if y in S else x, T, 0) if n*q < 10**6 else len(reduce(and_, [S, T]))