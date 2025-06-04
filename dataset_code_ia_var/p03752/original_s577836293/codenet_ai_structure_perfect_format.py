import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))
N_index = list(range(1, N))

min_cost = float('inf')
for target_indexes in itertools.combinations(N_index, K - 1):
    cost = 0
    copy_A = A.copy()
    for i in target_indexes:
        if copy_A[i] <= max(copy_A[:i]):
            diff = max(copy_A[:i]) - copy_A[i]
            copy_A[i] += diff + 1
            cost += diff + 1
    min_cost = min(min_cost, cost)

print(min_cost)