from dataclasses import dataclass
from math import hypot
from itertools import islice

@dataclass(frozen=True, slots=True)
class Wall:
    x: int
    y: int
    r: int

    def sign(self, px: int, py: int) -> int:
        return 1 if (dx := px - self.x)**2 + (dy := py - self.y)**2 > self.r**2 else -1

def is_visible(x1: int, y1: int, x2: int, y2: int, wall: Wall) -> bool:
    s1, s2 = wall.sign(x1, y1), wall.sign(x2, y2)
    if s1 == 1 and s2 == 1:
        # Equation of line: la*x + lb*y + lc = 0
        la, lb = y2 - y1, -(x2 - x1)
        lc = -x1 * la + y1 * (x2 - x1)
        # Distance from center to line
        dist2 = (la * wall.x + lb * wall.y + lc) ** 2
        norm2 = la ** 2 + lb ** 2
        if dist2 <= wall.r ** 2 * norm2:
            dx, dy = x2 - x1, y2 - y1
            ma, mb = dx, dy
            mc = -dx * wall.x - dy * wall.y
            test1 = ma * x1 + mb * y1 + mc
            test2 = ma * x2 + mb * y2 + mc
            return (test1 * test2) >= 0
        return True
    elif s1 == -1 and s2 == -1:
        return True
    return False

def main():
    import sys
    it = iter(sys.stdin.read().split())
    next_token = it.__next__
    while (n := int(next_token())) != 0:
        walls = [Wall(int(next_token()), int(next_token()), int(next_token())) for _ in range(n)]
        m = int(next_token())
        for _ in range(m):
            tx, ty, sx, sy = (int(next_token()) for _ in range(4))
            result = "Danger"
            for wall in walls:
                if not is_visible(tx, ty, sx, sy, wall):
                    result = "Safe"
                    break
            print(result)

if __name__ == "__main__":
    main()