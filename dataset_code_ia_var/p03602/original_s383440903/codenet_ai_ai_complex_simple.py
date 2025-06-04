from functools import reduce
from itertools import product, permutations, combinations, chain
import sys

N = int(sys.stdin.readline())
A = list(map(lambda _: list(map(int, sys.stdin.readline().split())), range(N)))

invalid = any(
    A[i][j] > A[i][k] + A[k][j]
    for k in range(N)
    for i in range(N)
    for j in range(N)
)
if invalid:
    print(-1)
    sys.exit()

get_sum = lambda acc, ij: acc + (0 if any(
    A[ij[0]][ij[1]] == A[ij[0]][k] + A[k][ij[1]] and k not in ij
    for k in range(N)) else A[ij[0]][ij[1]])
ans = reduce(get_sum, combinations(range(N), 2), 0)

print(ans)