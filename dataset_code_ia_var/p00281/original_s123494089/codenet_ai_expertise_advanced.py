from sys import stdin
from itertools import starmap

def main():
    n, m = map(int, stdin.readline().split())
    works = [[] for _ in range(n)]
    for line in stdin:
        s, *rest = map(int, line.split())
        if s == 0:
            break
        t, e = rest
        works[s - 1].append((t - 1, e))
    l = int(stdin.readline())
    blst_lines = [tuple(map(int, stdin.readline().split())) for _ in range(l)]
    for blst in blst_lines:
        print(*starmap(lambda idx, jobs: sum(blst[t] * e for t, e in jobs), enumerate(works)))
main()