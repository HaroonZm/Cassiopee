from sys import stdin
from itertools import starmap

def main():
    n, m = map(int, stdin.readline().split())
    works = [[] for _ in range(n + 1)]
    for line in stdin:
        s, *rest = map(int, line.split())
        if s == 0:
            break
        t, e = rest
        works[s].append((t - 1, e))
    l = int(stdin.readline())
    blsts = [tuple(map(int, stdin.readline().split())) for _ in range(l)]
    calc = lambda blst, i: sum(blst[t] * e for t, e in works[i])
    for blst in blsts:
        print(*starmap(lambda i: calc(blst, i), range(1, n + 1)))

main()