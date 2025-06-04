from sys import stdin, exit
from itertools import starmap

def main():
    input_iter = iter(stdin.readline, '')
    while True:
        N = int(next(input_iter))
        if N == 0:
            exit()
        W, H = map(int, next(input_iter).split())
        persimmon = [[0]*100 for _ in range(100)]
        for _ in range(N):
            x, y = map(int, next(input_iter).split())
            persimmon[x][y] = 1

        cumsum = [[0]*100 for _ in range(100)]
        for x in range(1, 100):
            row_persimmon = persimmon[x]
            row_cumsum = cumsum[x]
            row_cumsum_prev = cumsum[x-1]
            for y in range(1, 100):
                row_cumsum[y] = (
                    row_cumsum_prev[y]
                    + row_cumsum[y-1]
                    - row_cumsum_prev[y-1]
                    + row_persimmon[y]
                )

        S, T = map(int, next(input_iter).split())
        max_persimmon = max(
            cumsum[x][y] + cumsum[x-S][y-T] - cumsum[x][y-T] - cumsum[x-S][y]
            for x in range(S, W+1)
            for y in range(T, H+1)
        )
        print(max_persimmon)

if __name__ == '__main__':
    main()