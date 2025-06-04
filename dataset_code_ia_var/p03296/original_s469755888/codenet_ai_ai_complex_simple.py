from functools import reduce
from itertools import groupby, starmap
from operator import itemgetter, floordiv

N = int(input())
a = list(map(int, input().split()))

chunk_lengths = list(map(len, map(list, groupby(a))))
res = sum(starmap(floordiv, zip(chunk_lengths, [2]*len(chunk_lengths))))
print(res)