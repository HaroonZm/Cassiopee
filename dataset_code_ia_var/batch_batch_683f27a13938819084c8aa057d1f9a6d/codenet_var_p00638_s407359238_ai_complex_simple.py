from functools import reduce
from itertools import starmap, accumulate, takewhile, chain
import sys

def readint():
    return int(sys.stdin.readline())

def readtuple():
    return tuple(map(int, sys.stdin.readline().split()))

def main():
    from operator import itemgetter

    for _ in iter(int, 1):
        n = readint()
        if not n:
            break

        bridges = list(starmap(lambda t, b: (t, b), (readtuple() for _ in range(n))))
        order = sorted(bridges, key=itemgetter(1))

        cumul = list(accumulate(map(itemgetter(0), order)))
        oks = list(starmap(lambda acc, b: acc <= b, zip(cumul, map(itemgetter(1), order))))

        verdict = reduce(lambda x, y: x and y, oks, True)
        print(["No", "Yes"][verdict])

main()