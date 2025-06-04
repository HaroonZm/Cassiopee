import sys
import os
import math
import array
from fractions import Fraction
import functools
import itertools

DEBUG = os.environ.get('DEBUG', False)

inp = lambda: sys.stdin.readline().rstrip()
def read_int():
    return int(inp())
def read_ints():
    return list(map(int, inp().split()))

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def main():
    (R, S, P) = tuple(read_ints())
    records = []
    for dummy in range(P):
        x, y = read_ints()
        records.append((x-1, y-1))
    print(algorithmic_shuffle(R, S, P, records))

def algorithmic_shuffle(R, S, P, lst):
    # use a procedural initial
    q = array.array('i', (0 for _ in range(R+S+1)))
    for point in lst:
        i, j = point
        v = (S-j) if j < S else j-S+1
        q[R-1-i+v] += 1

    offset = 0
    for index in range(len(q)):
        c = q[index] + offset
        if c:
            q[index] = True
            offset = c - 1
        else:
            q[index] = False
    if offset:
        return R + S + 1 + offset

    def dropwhile_zero(arr):
        # demonstrate functional, but break early
        i = len(arr) - 1
        while i >= 0 and arr[i] == 0:
            arr.pop()
            i -= 1
        return arr

    q = dropwhile_zero(list(q))
    return len(q)

if __name__ == "__main__":
    main()