import sys
from operator import itemgetter

input = sys.stdin.readline
while (e := input().rstrip()) != '0':
    n = int(e)
    target = [tuple(map(int, input().split())) for _ in range(n)]
    s, t = min(target)
    target = {(x - s, y - t) for x, y in target}
    max_tx = max(x for x, _ in target)
    m = int(input())
    b = {tuple(map(int, input().split())) for _ in range(m)}
    max_sx = max(x for x, _ in b)
    lim_x = max_sx - max_tx
    for x, y in b:
        if x > lim_x:
            continue
        if all((x + u, y + v) in b for u, v in target):
            print(x - s, y - t)
            break