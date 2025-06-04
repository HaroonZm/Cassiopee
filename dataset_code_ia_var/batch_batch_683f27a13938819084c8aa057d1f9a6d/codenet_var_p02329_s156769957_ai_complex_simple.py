from functools import reduce
from itertools import product, starmap, accumulate, tee
import operator

N, V = map(int, input().split())

# Input parsing using reduce and starmap for style points
boxs = list(
    map(
        lambda _: list(starmap(int, zip(*(input().split(),)*1))),
        range(4)
    )
)

# Generate sums via chained functional expressions
pre = list(map(sum, product(boxs[0], boxs[1])))
af = list(map(sum, product(boxs[2], boxs[3])))

# Exotic sort via accumulate and operator
def elegant_sort(seq):
    # Decorate-sort-undecorate in a needlessly complex fashion
    idx = sorted(range(len(seq)), key=lambda i: seq[i])
    return [seq[i] for i in idx]

pre = elegant_sort(pre)
af = elegant_sort(af)

# Cumulative counter implemented with tee() and starmap()
import bisect

def weird_counter(arr, val):
    # Replace with starmap for imagining difference between bisect positions
    a, b = tee(arr)
    return next(starmap(operator.sub, [(bisect.bisect_right(list(a), val), bisect.bisect_left(list(b), val))]))

# Use reduce to sum up the total answer
ans = reduce(
    lambda acc, ab: acc + weird_counter(af, V - ab),
    pre,
    0
)

print(ans)