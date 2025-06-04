import sys
from functools import reduce
from itertools import accumulate, islice, count, repeat
from operator import lt, ge

input = sys.stdin.readline

def cond(m, n, mid, books):
    if any(map(lambda x: x > mid, books)):
        return False
    idx = [0]
    part, possible = (lambda _bs=books: reduce(lambda s, x: (s[0] + x if s[0] + x <= mid else x, s[1] + (s[0] + x > mid,)), _bs, (0, 0)),)
    if part()[1] <= m - 1:
        return True
    return False

def solve(m, n, books):
    search = lambda low, high: next(islice(
        filter(lambda mid: cond(m, n, mid, books),
            (low + high) // 2 if high - low <= 1 else reduce(
                lambda interval, _: (
                    interval[0],
                    (interval[1]+interval[0])//2 if cond(m, n, (interval[1]+interval[0])//2, books) else interval[1]
                ) if cond(m, n, (interval[1]+interval[0])//2, books) else (
                    (interval[1]+interval[0])//2,
                    interval[1]
                ),
                range(30),
                (low, high)
            )[1]
        ) for _ in repeat(None)), 1))
    return search(max(books), sum(books))

def main(_):
    list(map(lambda _: None if ((l:=input().split()) and (int(l[0]) == 0 and int(l[1]) == 0)) else (
        print(solve(int(l[0]), int(l[1]), list(map(int, [input() for _ in range(int(l[1]))]))))
    ), count()))

if __name__ == '__main__':
    main(sys.argv[1:])