n = int(input())
a, b = map(int, input().split())
c, d = map(int, input().split())

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

res = 10**9
for w in range(1, n + 1):
    def pos(i):
        i -= 1
        return (i % w, i // w)
    ax, ay = pos(a)
    bx, by = pos(b)
    cx, cy = pos(c)
    dx, dy = pos(d)
    res = min(res, dist(ax, ay, bx, by) + dist(cx, cy, dx, dy))

print(res)