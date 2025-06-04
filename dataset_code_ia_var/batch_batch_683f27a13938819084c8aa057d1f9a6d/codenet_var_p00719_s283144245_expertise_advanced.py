#!/usr/bin/env python3

import sys
import functools
import itertools
from math import inf

sys.setrecursionlimit(10 ** 6)

POWERS_OF_TWO = [1 << i for i in range(10)]

def solve(n, m, p, a, b):
    a -= 1
    b -= 1
    speeds = list(map(int, input().split()))
    adjacency = [[] for _ in range(m)]
    for _ in range(p):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        adjacency[x].append((y, z))
        adjacency[y].append((x, z))

    state_count = POWERS_OF_TWO[n]
    dp = [[inf] * m for _ in range(state_count)]
    dp[0][a] = 0

    # More concise iteration using enumerate and generator expressions
    for state, horse in itertools.product(range(state_count), range(n)):
        horse_mask = POWERS_OF_TWO[horse]
        if state & horse_mask:
            continue
        next_state = state | horse_mask
        for city in range(m):
            cost_so_far = dp[state][city]
            if cost_so_far == inf:
                continue
            for next_city, dist in adjacency[city]:
                travel_time = cost_so_far + dist / speeds[horse]
                if travel_time < dp[next_state][next_city]:
                    dp[next_state][next_city] = travel_time

    ans = min(dp[state][b] for state in range(state_count))
    print("Impossible" if ans == inf else ans)

def main():
    while True:
        try:
            n, m, p, a, b = map(int, input().split())
            if n == 0:
                break
            solve(n, m, p, a, b)
        except EOFError:
            break

if __name__ == "__main__":
    main()