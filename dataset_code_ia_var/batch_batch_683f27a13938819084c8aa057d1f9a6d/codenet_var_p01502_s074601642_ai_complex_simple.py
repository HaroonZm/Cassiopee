from functools import reduce
from itertools import combinations
N = int(raw_input())
cost = list(map(lambda x: list(map(int, x.split())), [raw_input() for _ in xrange(N)]))
all_cost = reduce(lambda acc, ij: acc + min(cost[ij[0]][ij[1]], cost[ij[1]][ij[0]]), combinations(range(N), 2), 0)
print all_cost