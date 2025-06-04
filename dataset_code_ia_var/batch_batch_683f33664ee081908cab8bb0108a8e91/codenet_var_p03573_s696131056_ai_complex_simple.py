from functools import reduce
from itertools import combinations

i = input().split()
idx = reduce(lambda a,b: a if sum(1 for x in i if x == i[a]) > 1 else b, range(3))
print(i[reduce(lambda a,b: b if b != idx and i.index(i[b]) == a else a, range(3))])