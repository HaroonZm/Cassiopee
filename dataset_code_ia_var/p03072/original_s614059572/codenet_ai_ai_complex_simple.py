from functools import reduce
from operator import itemgetter
from itertools import accumulate, count, takewhile

n = int(input())
L = list(map(int, input().split()))

indices = list(range(n))
pairs = zip(indices, L)
maxima = list(accumulate(L, max))

cnt = sum(map(lambda t: t[1] == t[2], zip(indices, L, maxima)))
print(cnt)