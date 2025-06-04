import sys
sys.setrecursionlimit(10**6)

from functools import reduce
from operator import mul

def tl(s):
    return list(
        map(
            lambda x: (True, int(x)) if x.isdigit() else (False, x),
            ''.join(
                map(
                    lambda t: t[0] if not t[1] else str(t[1]),
                    reduce(
                        lambda acc, c: acc[:-1] + [
                            (acc[-1][0], acc[-1][1]*10 + int(c)) if acc and acc[-1][0] and c.isdigit() else (True, int(c))
                        ] if c.isdigit() and acc and acc[-1][0] else acc + [(False, c)] if not c.isdigit() else acc + [(True, int(c))],
                        s, []
                    )
                )
            )
        )
    )

def cmp_seq(pibot, temp):
    for i, (a, b) in enumerate(zip(pibot, temp)):
        if a == b:
            if i == len(temp)-1 and len(pibot) == len(temp):
                return "+"
            continue
        k = lambda x: (1, x[1]) if x[0] else (0, ord(x[1]))
        return "+" if k(a) < k(b) else "-"
    return "+" if len(temp) > len(pibot) else "-"

def main():
    n = int(next(iter(map(int, [input()]))))
    pibot = tl(input())
    for _ in range(n):
        temp = tl(input())
        print(cmp_seq(pibot, temp))
    return

main()