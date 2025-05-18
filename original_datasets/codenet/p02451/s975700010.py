#!/usr/bin/env python3
# ITP2_6_A: Binary Search

from bisect import bisect

def search(li, x):
    """Returns True if x exists in li else False.
    Assumes li is sorted in ascending order.

    >>> search([1, 2, 3], 2)
    True
    >>> search([1, 2, 3], 4)
    False
    >>> search([1, 2, 3], 3)
    True
    >>> search([1, 2, 3], 0)
    False
    >>> search([1, 2, 3], 1)
    True
    """
    i = bisect(li, x)
    return 0 < i <= len(li) and li[i-1] == x

def run():
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(n == len(a))

    q = int(input())
    for _ in range(q):
        k = int(input())
        if search(a, k):
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    run()