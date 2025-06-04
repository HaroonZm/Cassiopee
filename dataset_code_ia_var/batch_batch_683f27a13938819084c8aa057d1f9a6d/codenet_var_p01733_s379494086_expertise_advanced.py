from collections import defaultdict
from itertools import product
from sys import stdin

def main():
    a = defaultdict(int)
    b = 0
    n = int(stdin.readline())
    for _ in range(n):
        x, y, w = map(int, stdin.readline().split())
        for dx, dy in product((0, 1), repeat=2):
            coord = (x + dx, y + dy)
            a[coord] += w
            b = max(b, a[coord])
    print(f'{b} / 1')

main()