from sys import stdin
from math import inf
from functools import partial

def main():
    readline = partial(next, iter(stdin))
    while True:
        try:
            N, M, P, A, B = map(int, readline().split())
        except StopIteration:
            break
        if not (N | M | P | A | B):
            break
        A, B = A - 1, B - 1
        T = list(map(int, readline().split()))
        dp = [[inf] * M for _ in range(1 << N)]
        dp[0][A] = 0.0
        edges = []
        for _ in range(P):
            s, t, c = map(int, readline().split())
            s -= 1; t -= 1
            edges.append((s, t, c))
            edges.append((t, s, c))

        for state in range(1 << N):
            sbits = [k for k in range(N) if (state >> k) & 1]
            for s, t, c in edges:
                for k in sbits:
                    prev = state & ~(1 << k)
                    val = dp[prev][s] + c / T[k]
                    if val < dp[state][t]:
                        dp[state][t] = val

        ans = min(dp[state][B] for state in range(1 << N))
        print("Impossible" if ans == inf else f"{ans:.5f}")

if __name__ == "__main__":
    main()