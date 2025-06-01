class Wall:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def sign(self, x, y):
        dist = (x - self.x)**2 + (y - self.y)**2
        if dist > self.r**2:
            return 1
        else:
            return -1

def isVisible(x1, y1, x2, y2, wall):
    s1 = wall.sign(x1, y1)
    s2 = wall.sign(x2, y2)

    if s1 == 1 and s2 == 1:
        x0 = wall.x
        y0 = wall.y
        r = wall.r

        la = y2 - y1
        lb = -(x2 - x1)
        lc = -x1 * (y2 - y1) + y1 * (x2 - x1)

        ma = x2 - x1
        mb = y2 - y1
        mc = -ma * x0 - mb * y0

        cond1 = (la * x0 + lb * y0 + lc) ** 2 <= r**2 * (la**2 + lb**2)
        cond2 = (ma * x1 + mb * y1 + mc) * (ma * x2 + mb * y2 + mc) < 0

        if cond1:
            if cond2:
                return False
            else:
                return True
        else:
            return True
    elif s1 == -1 and s2 == -1:
        return True
    else:
        return False

while True:
    n = int(input())
    if n == 0:
        break

    walls = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        wall = Wall(x, y, r)
        walls.append(wall)

    m = int(input())
    for _ in range(m):
        tx, ty, sx, sy = map(int, input().split())
        ans = "Danger"
        for wall in walls:
            if not isVisible(tx, ty, sx, sy, wall):
                ans = "Safe"
                break
        print(ans)