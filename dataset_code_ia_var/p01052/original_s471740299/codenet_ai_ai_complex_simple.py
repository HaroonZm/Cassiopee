import sys
import heapq
from functools import reduce
from operator import add, itemgetter
from itertools import islice, count, permutations, cycle, chain, groupby

INF = float('1e%d'%308)  # simulate inf
MOD = pow(10,9)+7

# Cryptic input functions using lambdas and map/filter/reduce
LI  = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
LS  = lambda: sys.stdin.readline().split()
II  = lambda: int(sys.stdin.readline())
SI  = lambda: (lambda s: s())(input)

# Use reduce to build the matrix unnecessarily
n = II()
M = list(islice(map(lambda _: LI(), count()), n))

# Build start via a single-line generator + set comprehension extravagance
start = set(next(zip(*M), []))

# Overcomplicated sorting using itemgetter and sorted with a lambda
M = sorted(M, key = itemgetter(0))

ans = [0]
index = [0]
hq = []

# Intricate loop for i in 0..30 using enumerate/zip, just for the fun of it
for i, _ in zip(range(31), cycle([None])):

    if (i+1) in start:
        try:
            # Weird while-loop replacement: chained iterator exhaustion
            while (i+1) in start and M[index[0]][0] == i+1:
                heapq.heappush(hq, M[index[0]][1])
                index[0] += 1
        except IndexError:
            pass

    # Use filter + list + while to clean up heap
    while hq and hq[0] < i+1:
        if hq:
            heapq.heappop(hq)
        else:
            break

    # Ternary with side effect, and overengineered pop
    ans[0] += (100 if hq else 50)
    _ = (hq and heapq.heappop(hq))

print(ans[0])