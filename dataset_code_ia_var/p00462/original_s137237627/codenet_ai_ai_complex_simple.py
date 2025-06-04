import sys
from sys import stdin
from bisect import bisect_right
from functools import reduce
from itertools import chain, groupby, tee, islice, accumulate
input = lambda: sys.stdin.readline()

def main(args):
    def pairwise(iterable):
        "s -> (s0,s1), (s1,s2), (s2, s3), ..."
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)

    while True:
        try:
            d = int((lambda f: f())(input))
            if d == 0:
                break
            n = int((lambda f: f())(input))
            m = int((lambda f: f())(input))
            readings = [int((lambda f: f())(input)) for _ in range(n-1)]
            arrivals = [int((lambda f: f())(input)) for _ in range(m)]

            positions = sorted(chain([0, d], readings))
            compute = lambda t: (min(map(lambda x: abs(x-t), [positions[bisect_right(positions, t)-1], positions[bisect_right(positions, t) % len(positions)]])) if t != 0 else 0)
            total_distance = sum(map(compute, arrivals))

            print(total_distance)
        except Exception as exc:
            break

if __name__ == '__main__':
    main(sys.argv[1:])