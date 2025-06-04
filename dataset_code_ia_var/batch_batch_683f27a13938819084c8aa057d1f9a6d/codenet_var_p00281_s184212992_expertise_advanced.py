from sys import stdin
from itertools import starmap

def main():
    lines = iter(stdin.read().splitlines())
    while True:
        try:
            n, m = map(int, next(lines).split())
        except StopIteration:
            break
        rs = []
        for line in lines:
            if line == "0 0 0":
                break
            rs.append(tuple(map(int, line.split())))
        l = int(next(lines))
        b = [list(map(int, next(lines).split())) for _ in range(l)]
        c = [[0] * n for _ in range(l)]
        for s, t, e in rs:
            s, t = s - 1, t - 1
            for i in range(l):
                c[i][s] += b[i][t] * e
        print('\n'.join(' '.join(map(str, row)) for row in c))

if __name__ == "__main__":
    main()