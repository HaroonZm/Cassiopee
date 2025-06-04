from sys import stdin
from collections import Counter

def min_steps_to_equal(triple):
    # Using memoization to cache already computed states
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(x, y, z):
        a, b, c = sorted((x, y, z))
        if a == b == c:
            return 0
        # Two cases: increase a by 2, or increase a and b by 1
        if b == c:
            return 1 + dp(a + 2, b, c)
        else:
            return 1 + dp(a + 1, b + 1, c)
    return dp(*triple)

if __name__ == '__main__':
    triple = tuple(map(int, stdin.readline().split()))
    print(min_steps_to_equal(triple))