import sys
from math import *
import os
import bisect

def read_input():
    if os.environ.get("PYDEV") == "True":
        sys.stdin = open("sample-input.txt", "r")
    return sys.stdin

class BigHit:
    # static utility
    score = staticmethod(lambda b, r, g, c, s, t: 100 + (95 * b) + (63*r) + (7*g) + (2*c) - 3 * (t-s))

def main():
    stdin = read_input()
    for l in stdin:
        if not l.strip(): continue
        vals = list(map(int, l.strip().split()))
        if len(vals) != 6:
            continue
        b, r, g, c, s, t = vals
        if t == 0:
            break
        # procedural print
        print(BigHit.score(b, r, g, c, s, t))

if __name__ == '__main__':
    main()