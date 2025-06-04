#!/usr/bin/env python3
# ITP2_11_D: Bitset 2 - Enumeration of Combinations

def combination(n, k):
    """Yields all combinations of k numbers from n numbers.

    >>> list(combination(3, 2))
    [[0, 1], [0, 2], [1, 2]]
    """
    def _combination(i, j, a):
        if i > n:
            return
        if j == 0:
            yield nums(n, a)
        elif i <= n:
            yield from _combination(i + 1, j - 1, a | (1 << i))
            yield from _combination(i + 1, j, a)
    yield from _combination(0, k, 0)

def nums(size, bit):
    """Returns list of bit positions where bit flag is on.

    >>> nums(4, 7)
    [0, 1, 2]
    """
    return [n for n in range(size) if bit & (1 << n)]

def bit(nums):
    """Returns a bit representation of nums.

    >>> bit([0, 1, 2])
    7
    """
    return sum(1 << n for n in nums)

def run():
    n, k = [int(i) for i in input().split()]
    for ns in sorted(combination(n, k), key=bit):
        print("{}: {}".format(bit(ns), " ".join(str(i) for i in ns)))

if __name__ == '__main__':
    run()