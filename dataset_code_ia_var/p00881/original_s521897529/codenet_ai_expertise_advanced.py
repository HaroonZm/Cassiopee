from collections import Counter
from functools import partial

def solve():
    get_ints = lambda: map(int, input().split())
    while True:
        m, n = get_ints()
        if not m:
            break
        objs = [int(input(), 2) for _ in range(n)]
        N = 1 << m
        bits = [1 << i for i in range(m)]
        dp = [bytearray(N) for _ in range(N)]

        # Precompute candidates for masks to avoid recomputation in inner loop
        for mask in reversed(range(N - 1)):
            relevant = Counter(obj & mask for obj in objs)
            for masked, cnt in relevant.items():
                if cnt > 1:
                    candidates = (b for b in bits if not b & mask)
                    dp_vals = (max(dp[mask | b][masked], dp[mask | b][masked | b]) + 1 for b in candidates)
                    try:
                        dp[mask][masked] = min(dp_vals)
                    except ValueError:
                        pass  # min(empty) for masks with no candidates
        print(dp[0][0])

solve()