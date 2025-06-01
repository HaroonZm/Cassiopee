#!/usr/bin/env python
import string
import sys
from itertools import chain, takewhile

def read(f, *shape, it=chain.from_iterable(sys.stdin), whitespaces=set(string.whitespace)):
    def read_word():
        return f("".join(takewhile(lambda c: c not in whitespaces, it)).strip())

    if not shape:
        return read_word()
    elif len(shape) == 1:
        return [read_word() for _ in range(shape[0])]
    elif len(shape) == 2:
        return [[read_word() for _ in range(shape[1])] for _ in range(shape[0])]

def arr(*shape, fill_value=0):
    if len(shape) == 1:
        return [fill_value] * shape[0]
    elif len(shape) == 2:
        return [[fill_value] * shape[1] for _ in range(shape[0])]

def debug(**kwargs):
    print(
        ", ".join("{} = {}".format(k, repr(v)) for k, v in kwargs.items()),
        file=sys.stderr,
    )

def main():
    while True:
        h, w, n = map(int, sys.stdin.readline().split())
        if (h, w, n) == (0, 0, 0):
            return
        grid = []
        for _ in range(h):
            row = list(map(int, sys.stdin.readline().split()))
            grid.append(row)

        dp = arr(h, w)
        dp[0][0] = n - 1

        for i in range(h):
            for j in range(w):
                if i < h - 1 and grid[i][j] == 0:
                    dp[i + 1][j] += (dp[i][j] + 1) // 2
                if i < h - 1 and grid[i][j] == 1:
                    dp[i + 1][j] += dp[i][j] // 2
                if j < w - 1 and grid[i][j] == 0:
                    dp[i][j + 1] += dp[i][j] // 2
                if j < w - 1 and grid[i][j] == 1:
                    dp[i][j + 1] += (dp[i][j] + 1) // 2

        for i in range(h):
            for j in range(w):
                grid[i][j] = (grid[i][j] + dp[i][j]) % 2

        i = 0
        j = 0
        while i < h and j < w:
            if grid[i][j] == 0:
                i += 1
            else:
                j += 1
        print(i + 1, j + 1)

if __name__ == "__main__":
    main()