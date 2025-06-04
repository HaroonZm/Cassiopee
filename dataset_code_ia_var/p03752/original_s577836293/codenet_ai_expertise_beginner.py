N, K = map(int, input().split())
A = list(map(int, input().split()))
N_index = []
for i in range(1, N):
    N_index.append(i)

min_cost = 10**18
from itertools import combinations

for comb in combinations(N_index, K - 1):
    cost = 0
    copy_A = A[:]
    for i in comb:
        left_max = max(copy_A[:i])
        if copy_A[i] <= left_max:
            add = left_max - copy_A[i] + 1
            copy_A[i] += add
            cost += add
    if cost < min_cost:
        min_cost = cost

print(min_cost)