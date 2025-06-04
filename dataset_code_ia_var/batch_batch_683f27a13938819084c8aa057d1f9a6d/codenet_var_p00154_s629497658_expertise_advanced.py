import sys
from sys import stdin
from functools import lru_cache

input = stdin.readline

def solve(m, cards, g, guesses):
    cards = [(0, 0), *sorted(cards)]
    max_guess = max(guesses) if guesses else 0
    W = max_guess + 1

    # Use a 1D dp array; optimized bounded knapsack by iterating over cards and using min(count, needed)
    dp = [0] * W
    dp[0] = 1
    for value, count in cards[1:]:
        if value == 0:
            continue
        ndp = dp[:]
        for rem in range(1, count + 1):
            step = value * rem
            for j in range(step, W):
                ndp[j] += dp[j - step]
        dp = ndp

    return [dp[q] for q in guesses]

def main(args):
    while True:
        m = int(input())
        if m == 0:
            break
        cards = [tuple(map(int, input().split())) for _ in range(m)]
        g = int(input())
        guesses = [int(input()) for _ in range(g)]
        print('\n'.join(map(str, solve(m, cards, g, guesses))))

if __name__ == '__main__':
    main(sys.argv[1:])