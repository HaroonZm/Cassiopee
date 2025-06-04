from functools import reduce
import operator
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
points = list(map(lambda _: tuple(map(int, input().split())), range(N)))

def half(n): return n // 2
def check_even(n):
    return n & 1 == 0

if not check_even(N):
    print("NA")
    sys.exit()

indices = [(i, i + half(N)) for i in range(half(N))]
pairs = list(map(lambda idx: (points[idx[0]], points[idx[1]]), indices))
sum_pairs = list(map(lambda pr: tuple(map(operator.add, pr[0], pr[1])), pairs))

ans = sum_pairs[0]
if not reduce(lambda acc, s: acc and s == ans, sum_pairs[1:], True):
    print("NA")
    sys.exit()

mid = tuple(map(lambda x: x / 2.0, ans))
print("{0} {1}".format(*mid))