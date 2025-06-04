import sys
input = sys.stdin.readline

from functools import reduce
from itertools import islice, cycle, starmap, repeat

def main():
    N = int(next(iter(map(str.strip, iter(input, '')))))
    A = list(map(int, next(iter(map(str.strip, iter(input, '')))).split()))

    S = reduce(lambda x, y: x + y, A)
    F = N * (N + 1) // 2

    verdict = lambda x: print("YES") if x else print("NO")

    def get_t():
        q, r = divmod(S, F)
        return q if r == 0 else None

    t = get_t()
    if t is None:
        return verdict(False)

    diff = lambda i: A[i] - A[i-1] - t
    indices = islice(cycle(range(N)), N)
    D = list(map(diff, indices))

    cond = all(map(lambda x: x <= 0 and x % N == 0, D))
    verdict(cond)

if __name__ == '__main__':
    main()