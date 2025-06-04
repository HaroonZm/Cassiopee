from functools import partial
from operator import itemgetter
from sys import stdin

def func(s, a, b, c):
    return s, int(a) * 3 + int(c)

parse_line = lambda line: func(*line.split())

def main():
    lines = iter(stdin.readline, '')
    n = int(next(lines))
    while n:
        data = [parse_line(next(lines)) for _ in range(n)]
        for s, p in sorted(data, key=itemgetter(1), reverse=True):
            print(f"{s},{p}")
        n = int(next(lines, '0'))
        if n != 0:
            print()

if __name__ == '__main__':
    main()