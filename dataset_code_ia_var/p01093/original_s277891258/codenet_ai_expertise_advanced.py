from sys import stdin
from itertools import tee

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2,s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def min_diff(arr):
    return min((b - a for a, b in pairwise(arr)), default=arr[-1])

def main():
    lines = map(str.strip, stdin)
    results = []
    it = iter(lines)
    while True:
        try:
            n = int(next(it))
            if n == 0:
                break
            a = sorted(map(int, next(it).split()))
            results.append(min_diff(a))
        except StopIteration:
            break
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()