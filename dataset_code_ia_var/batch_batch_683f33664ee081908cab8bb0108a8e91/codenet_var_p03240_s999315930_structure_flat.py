import sys
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N = int(sys.stdin.readline().strip())
XYH = []
for i in range(N):
    x, y, h = map(int, sys.stdin.readline().strip().split())
    XYH.append((x, y, h))

for y1 in range(101):
    for x1 in range(101):
        H = set()
        for x2, y2, h in XYH:
            tmph = abs(x1 - x2) + abs(y1 - y2) + h
            if h > 0:
                H.add(tmph)
        if len(H) == 1:
            ansh = list(H)[0]
            ok = True
            for x2, y2, h in XYH:
                expected = max(ansh - (abs(x1 - x2) + abs(y1 - y2)), 0)
                if expected != h:
                    ok = False
                    break
            if ok:
                print(x1, y1, ansh)
                sys.exit()