"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0126

"""
import sys
from sys import stdin
from collections import defaultdict
input = stdin.readline

def solve(data):
    status = [[' '] * 9 for _ in range(9)]

    # ?¨???????????????§??????
    for y, row in enumerate(data):
        freq = defaultdict(int)
        for i, n in enumerate(row):
            if n in freq:
                freq[n].append(i)
            else:
                freq[n] = [i]
        for k, v in freq.items():
            if len(v) > 1:
                for ind in v:
                    status[y][ind] = '*'

    # ?????????????????§??????
    for x in range(9):
        freq = defaultdict(int)
        for y in range(9):
            n = data[y][x]
            if n in freq:
                freq[n].append(y)
            else:
                freq[n] = [y]
        for k, v in freq.items():
            if len(v) > 1:
                for ind in v:
                    status[ind][x] = '*'

    # 3x3????????§??????
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            freq = defaultdict(int)
            for yy in range(3):
                for xx in range(3):
                    n = data[y+yy][x+xx]
                    if n in freq:
                        freq[n].append((x+xx, y+yy))
                    else:
                        freq[n] = [(x+xx, y+yy)]

            for k, v in freq.items():
                if len(v) > 1:
                    for xx, yy in v:
                        status[yy][xx] = '*'

    for y in range(9):
        for x in range(9):
            print('{}{}'.format(status[y][x], data[y][x]), end='')
        print()

def main(args):
    n = int(input())
    for i in range(n):
        data = [[int(x) for x in input().split()] for _ in range(9)]
        result = solve(data)
        if i != n-1:
            print()

if __name__ == '__main__':
    main(sys.argv[1:])