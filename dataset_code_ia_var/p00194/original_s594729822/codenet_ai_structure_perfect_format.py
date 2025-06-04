from heapq import heappop, heappush
from string import ascii_lowercase as al

dic = dict([(c, i) for i, c in enumerate(al)])

def f(x):
    h, v = x
    return (dic[h], int(v) - 1)

def g(s):
    return f(s.split("-"))

def solve():
    hq = [(0, start[0], start[1])]
    while len(hq) != 0:
        cost, cy, cx = heappop(hq)
        if (cy, cx) == goal:
            return cost
        if (cost, cy, cx) in memo:
            continue
        memo[(cost, cy, cx)] = True
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < M and 0 <= nx < N:
                nc = condition[ny][nx][cy][cx] + D + cost
                if field[ny][nx] == 0:
                    heappush(hq, (nc, ny, nx))
                else:
                    if dy == 0:
                        if (nc // field[ny][nx]) % 2 == 1:
                            heappush(hq, (nc, ny, nx))
                    else:
                        if (nc // field[ny][nx]) % 2 == 0:
                            heappush(hq, (nc, ny, nx))

while True:
    M, N = map(int, raw_input().split())
    if M | N == 0:
        break
    memo = {}
    D = input()
    field = [[0] * N for _ in xrange(M)]
    condition = [[[[0] * N for _ in xrange(M)] for _ in xrange(N)] for _ in xrange(M)]
    for _ in xrange(input()):
        p, k = raw_input().split()
        h, v = g(p)
        field[h][v] = int(k)
    for _ in xrange(input()):
        (h1, v1), (h2, v2) = map(g, raw_input().split())
        condition[h1][v1][h2][v2] = condition[h2][v2][h1][v1] = 1 << 30
    for _ in xrange(input()):
        p1, p2, d = raw_input().split()
        h1, v1 = g(p1)
        h2, v2 = g(p2)
        condition[h1][v1][h2][v2] = condition[h2][v2][h1][v1] = int(d)
    start, goal = map(g, raw_input().split())
    print solve()