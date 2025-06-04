from functools import reduce
from itertools import chain, zip_longest

n = int(input())
a = sorted(map(int, input().split()), reverse=True)

pairwise = list(zip_longest(a[::2], a[1::2], fillvalue=0))
scores = reduce(lambda acc, ab: (acc[0]+ab[0], acc[1]+ab[1]), pairwise, (0,0))
print(reduce(lambda x, y: x - y, scores))