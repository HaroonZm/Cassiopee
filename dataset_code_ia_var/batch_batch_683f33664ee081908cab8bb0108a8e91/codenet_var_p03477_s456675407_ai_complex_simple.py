from functools import reduce
from operator import add, itemgetter

L = list(map(int, input().split()))
pairs = ((0,1),(2,3))
sums = list(map(lambda idx: reduce(add, map(itemgetter(*idx), [L])), pairs))

cmp_result = (sums[0] > sums[1]) - (sums[0] < sums[1])
print({0: "Balanced", 1: "Left", -1: "Right"}[cmp_result])