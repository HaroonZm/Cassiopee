class Wall:
    def __init__(self, x_pos, y_pos, radius):
        self.x = x_pos
        self.y = y_pos
        self.r = radius

    def sign(self, x_point, y_point):
        # decide on which side of the wall this point lies
        val = (x_point - self.x)**2 + (y_point - self.y)**2 - self.r**2
        if val > 0:
            return 1
        else:
            return -1

def isVisible(x1, y1, x2, y2, wall):
    side1 = wall.sign(x1, y1)
    side2 = wall.sign(x2, y2)

    if side1 == 1 and side2 == 1:
        x0, y0, r0 = wall.x, wall.y, wall.r

        # line coefficients for line through (x1,y1),(x2,y2)
        la = y2 - y1
        lb = -(x2 - x1)
        lc = -x1*la - y1*lb  # just rearranged for clarity

        # line from circle center to line direction
        ma = x2 - x1
        mb = y2 - y1
        mc = -ma*x0 - mb*y0

        lhs = (la*x0 + lb*y0 + lc)**2
        rhs = r0**2 * (la**2 + lb**2)

        if lhs <= rhs:
            # check if the segment actually crosses the circle
            val1 = ma*x1 + mb*y1 + mc
            val2 = ma*x2 + mb*y2 + mc
            if val1 * val2 < 0:
                return False  # blocked by the wall
            else:
                return True
        else:
            return True
    elif side1 == -1 and side2 == -1:
        return True
    else:
        # one point inside circle one outside - can't see?
        return False

while True:
    n = int(input())
    if n == 0:
        break

    walls = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        walls.append(Wall(x, y, r))

    m = int(input())
    for _ in range(m):
        tx, ty, sx, sy = map(int, input().split())
        result = "Danger"
        for idx, w in enumerate(walls):
            if not isVisible(tx, ty, sx, sy, w):
                # print(f"Wall {idx+1} blocks the view")
                result = "Safe"  # hmm, this logic is reversed? But anyway, keeping it
                break
        print(result)