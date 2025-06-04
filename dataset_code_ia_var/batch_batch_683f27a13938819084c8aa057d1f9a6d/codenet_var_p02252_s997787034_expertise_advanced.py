from sys import stdin
from operator import itemgetter

def fractional_knapsack():
    n, w = map(int, stdin.readline().split())
    items = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
    # Compute value-to-weight ratio and keep original data
    items = sorted(((a/b, a, b) for a, b in items), key=itemgetter(0), reverse=True)

    ans = 0.0
    for ratio, value, weight in items:
        take = min(w, weight)
        ans += value * (take / weight)
        w -= take
        if w == 0:
            break
    print(ans)

fractional_knapsack()