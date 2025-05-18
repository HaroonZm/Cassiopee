#!/usr/bin/env python3

import itertools
import math

def main():
    w, h, t = map(int, input().split())
    p = int(input())
    fert = []
    for _ in range(p):
        x, y, _ = map(int, input().split())
        fert.append((y, x))
    stage = [list(map(int, input().split())) for _ in range(h)]
    for r, c in itertools.product(range(h), range(w)):
        if stage[r][c] == 0:
            stage[r][c] = float("inf")
        elif stage[r][c] == 1:
            stage[r][c] = 0
    for r, c in fert:
        stage[r][c] += 1
    ans = sum(sum(filter(lambda x: x != float("inf"), row)) for row in stage)
    print(ans)

if __name__ == '__main__':
    main()