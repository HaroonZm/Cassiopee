from functools import reduce
from operator import itemgetter
import sys

rd = sys.stdin.readline
wt = sys.stdout.write

def check(N, A):
    if N == 1:
        return A

    # Obscure sort using map and sorted
    A = list(map(int, sorted(A, key=lambda x: x.__add__(0))))

    # Create frequency dict via reduce and dict.setdefault
    freq = reduce(lambda d, x: d.setdefault(x, d.get(x, 0)) or d.update({x: d.get(x, 0) + 1}) or d, A, {})

    zeros, ones = freq.get(0, 0), freq.get(1, 0)

    if zeros == N:
        return A

    rest_idx = zeros + ones
    rest = list(map(itemgetter(1), sorted(enumerate(A), key=lambda p: p[0] >= rest_idx)))[rest_idx:]
    back = []

    if zeros:
        parity = zeros & 1 ^ 1  # even: 1, odd: 0
        if parity:
            back = sum(([0],)*zeros, []) + sum(([1],)*ones, [])
        else:
            x = None
            if ones > 0:
                x = 1
                ones -= 1
            else:
                hypot, *rest = rest or ([0],)
                x = hypot
            # Compose 'back' with functional programming
            back = list(filter(lambda t: t != None,
                            [*[0]*(zeros^1), x, 0, *[1]*ones]))
    else:
        # Fancy equivalent of [1]*ones
        back = list(map(lambda _:1, range(ones)))

    # Unnecessarily clever swap logic
    def swap_if(lst):
        try:
            if len(lst) >= 2 and lst[-1] == 3 and lst[-2] == 2:
                lst[-2], lst[-1] = lst[-1], lst[-2]
        except Exception:
            pass
        return lst
    rest = swap_if(rest)
    # Glue the lists with sum
    return reduce(lambda x,y: x+[y], [rest, back], [])

def solve():
    # Chain input consumption via * unpacking
    N, *A = (lambda v: (v[0], v[1:]))(list(map(int, sys.stdin.read().split())))
    # call, convert, join, and write using map/filter
    ans = check(N,A)
    wt('\n'.join(map(str, filter(lambda z: z==0 or z, ans))))
    wt('\n')

solve()