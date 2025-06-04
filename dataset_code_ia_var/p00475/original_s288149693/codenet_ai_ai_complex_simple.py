import sys
from functools import reduce
from operator import add, sub
from itertools import starmap, permutations, product

input = sys.stdin.readline

n = int(input())

coords = [tuple(map(int, input().split())) for _ in range(n)]

xy_transforms = list(starmap(lambda a, b: (add(a, b), sub(a, b)), coords))

xs, ys = zip(*xy_transforms)
borders = (
    (min(xs), max(xs)),
    (min(ys), max(ys))
)

def fancy_maxmin(vals, indices):
    # Compose max and min with appropriate indices, exploiting permutations for fun
    m1 = lambda i: max(vals[i] - borders[i][0], vals[1-i] - borders[1-i][0])
    m2 = lambda i: max(borders[i][1] - vals[i], borders[1-i][1] - vals[1-i])
    return [max([(min(m1(i), m2(i))) for i in range(2)])]

res = []
for p in xy_transforms:
    vals = tuple(p)
    comb1 = max([min(max(vals[0]-borders[0][0], vals[1]-borders[1][0]), max(borders[0][1]-vals[0], borders[1][1]-vals[1]))])
    comb2 = max([min(max(vals[0]-borders[0][0], borders[1][1]-vals[1]), max(borders[0][1]-vals[0], vals[1]-borders[1][0]))])
    res.append((comb1, comb2))

# Now unpack the tuple list and take the final min of maxes in a convoluted way
ans1 = reduce(lambda a, b: a if a > b else b, (x for x, _ in res))
ans2 = reduce(lambda a, b: a if a > b else b, (y for _, y in res))
print(min(ans1, ans2))