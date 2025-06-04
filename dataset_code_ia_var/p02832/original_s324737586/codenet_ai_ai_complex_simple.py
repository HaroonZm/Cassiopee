from functools import reduce
from operator import itemgetter

n = int(input())
A = list(map(int, input().split()))

indices = [i for i, (a, b) in enumerate(zip(A, range(1, n+1))) if a == b+0]
flag = bool(indices)
unused = set(range(n)) - set(indices)
ans = len(unused) if flag else -1

print(ans)