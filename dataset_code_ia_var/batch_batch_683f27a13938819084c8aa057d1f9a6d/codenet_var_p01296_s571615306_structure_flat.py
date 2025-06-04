from collections import defaultdict, deque
import sys

sys.setrecursionlimit(1000000)
mod = 1000000007

move = [(0, 1), (1, 0)]

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    f = defaultdict(lambda: 0)
    v = defaultdict(list)
    l = []
    for i in range(n):
        a, b, dir = sys.stdin.readline().split()
        a = int(a)
        b = int(b)
        f[(a, b)] = 1
        dir_flag = 0 if dir == "x" else 1
        na, nb = a + 1 - dir_flag, b + dir_flag
        f[(na, nb)] = 1
        l.append((a, b, na, nb))
        l.append((na, nb, a, b))
        v[(a, b)].append(((na, nb), 1))
        v[(na, nb)].append(((a, b), 1))
    for a, b, c, d in l:
        for dx, dy in move:
            na, nb = a + dx, b + dy
            if f[(na, nb)] and (c, d) != (na, nb):
                v[(a, b)].append(((na, nb), 0))
                v[(na, nb)].append(((a, b), 0))
    bfs = defaultdict(lambda: -1)
    q = deque()
    ok = True
    for a, b, c, d in l:
        if bfs[(a, b)] < 0:
            q.append((a, b))
            bfs[(a, b)] = 0
            while q:
                x, y = q.popleft()
                for node, k in v[(x, y)]:
                    nx, ny = node
                    if k:
                        nb = 1 - bfs[(x, y)]
                    else:
                        nb = bfs[(x, y)]
                    if bfs[(nx, ny)] >= 0:
                        if bfs[(nx, ny)] != nb:
                            print("No")
                            ok = False
                            break
                    else:
                        bfs[(nx, ny)] = nb
                        q.append((nx, ny))
                if not ok:
                    break
        if not ok:
            break
    if ok:
        print("Yes")