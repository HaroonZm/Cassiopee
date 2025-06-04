from functools import reduce
from itertools import combinations
A, B, C = map(int, input().split())
lst = [A, B, C]
id_diff = next(filter(lambda t: len(set(t[1])) == 1, enumerate(combinations(lst, 2))))
print(reduce(lambda x, y: x^y, lst) ^ (id_diff[1][0] if id_diff[1][0] == id_diff[1][1] else 0))