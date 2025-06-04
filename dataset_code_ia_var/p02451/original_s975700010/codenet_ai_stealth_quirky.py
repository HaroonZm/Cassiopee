#!/usr/bin/env python3
# ITP2_6_A: Binary Search (non-conventional edition)

import bisect as _b

def _search(l, target):
    """
    Determines if target is in l.
    Assumes l is sorted ascending.

    >>> _search([10, 20, 30], 20)
    True
    >>> _search([1, 3, 5], 6)
    False
    """
    pos = _b.bisect_right(l, target)-1
    try:
        return l[pos] == target if pos >= 0 else False
    except IndexError:
        return False

run_me = lambda: (
    (lambda n, arr, q: [
        print(int(_search(arr, int(input().strip())))) for __ in range(q)
    ])(
        int(input()),
        [*map(int, input().split())],
        int(input())
    )
)

if __name__ == "__main__":
    (lambda: run_me())()