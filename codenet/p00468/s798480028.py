import sys
import itertools
readline = sys.stdin.readline

while True:
    N = int(readline())
    M = int(readline())
    if N == 0 and M == 0:
        break
    pairs = set()
    for _ in xrange(M):
        a, b = tuple(int(x) for x in readline().split())
        pairs.add((a, b))
        pairs.add((b, a))
    cnt = 0
    for i in xrange(2, N + 1):
        if (1, i) in pairs:
            cnt += 1
        else:
            for j in xrange(2, N + 1):
                if (1, j) in pairs and (j, i) in pairs:
                    cnt += 1
                    break
    print cnt