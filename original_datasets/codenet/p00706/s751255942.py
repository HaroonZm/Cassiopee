import sys
import collections

while True:
    N = int(raw_input())
    if N == 0:
        break
    W, H = map(int, sys.stdin.readline().split())
    area = [[0 for i in xrange(H)] for j in xrange(W)]
    for z in xrange(N):
        x, y = map(int, sys.stdin.readline().split())
        area[x - 1][y - 1] = 1
    S, T = map(int, sys.stdin.readline().split())
#    col = [[0 for i in xrange(H)] for j in xrange(W)]
#    row = [[0 for i in xrange(H)] for j in xrange(W)]
    max = -1
    for x in xrange(W - S + 1):
        for y in xrange(H - T + 1):
            sum = 0
            for s in xrange(S):
                for w in xrange(T):
                    sum += area[x + s][y + w]
            if sum > max:
                max = sum
    print max