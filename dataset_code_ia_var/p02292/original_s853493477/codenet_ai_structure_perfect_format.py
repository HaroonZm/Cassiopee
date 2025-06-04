import math

eps = 10 ** -8

line = input()
x1, y1, x2, y2 = list(map(int, line.split()))
line = input()
q = int(line)
pts = []
for _ in range(q):
    line = input()
    x, y = list(map(int, line.split()))
    pts.append([x, y])

def solve():
    l1 = math.hypot(x2 - x1, y2 - y1)
    for x, y in pts:
        l2 = math.hypot(x - x1, y - y1)
        dx = (x2 - x1) / l1
        dy = (y2 - y1) / l1
        ip = (x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)
        sine = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)
        if sine < 0.0:
            print("COUNTER_CLOCKWISE")
        elif sine > 0.0:
            print("CLOCKWISE")
        elif abs(ip - l1 * l2) < eps:
            if l1 < l2:
                print("ONLINE_FRONT")
            else:
                print("ON_SEGMENT")
        elif ip + l1 * l2 < eps:
            print("ONLINE_BACK")

solve()