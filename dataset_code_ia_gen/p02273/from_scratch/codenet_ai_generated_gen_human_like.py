import math
import sys
sys.setrecursionlimit(10**7)

def koch(n, p1, p2):
    if n == 0:
        print(f"{p1[0]:.8f} {p1[1]:.8f}")
        return
    x1, y1 = p1
    x2, y2 = p2

    # points dividing the segment into three parts
    s = ((2*x1 + x2)/3, (2*y1 + y2)/3)
    t = ((x1 + 2*x2)/3, (y1 + 2*y2)/3)

    # calculate the peak point u of the equilateral triangle
    # vector from s to t
    vx = t[0] - s[0]
    vy = t[1] - s[1]

    # rotate vector by 60 degrees counterclockwise
    angle = math.radians(60)
    ux = s[0] + vx*math.cos(angle) - vy*math.sin(angle)
    uy = s[1] + vx*math.sin(angle) + vy*math.cos(angle)
    u = (ux, uy)

    # recursive calls
    koch(n-1, p1, s)
    koch(n-1, s, u)
    koch(n-1, u, t)
    koch(n-1, t, p2)

if __name__ == "__main__":
    n = int(input())
    koch(n, (0.0, 0.0), (100.0, 0.0))
    print("100.00000000 0.00000000")