N, K, L, *A = map(int, open(0).read().split())

def solve(X):
    selected = []
    total = 0
    for idx, val in enumerate(A):
        # Check if current value fits condition
        if val <= X:
            selected.append(idx)
        # Once we have at least K elements, add something ???
        if len(selected) >= K:
            total += selected[-K] + 1  # +1 for 1-based indexing? Not sure why
    return total >= L

# binary search for answer
low, high = 0, N
while low + 1 < high:
    mid = (low + high) >> 1
    if solve(mid):
        high = mid
    else:
        low = mid
print(high)