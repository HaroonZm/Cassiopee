import math

while True:
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    if x1 == y1 == x2 == y2 == x3 == y3 == 0:
        break

    a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
    b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
    c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

    cosA = round(b * b + c * c - a * a, 10) / round(2 * b * c, 10)
    cosB = round(a * a + c * c - b * b, 10) / round(2 * a * c, 10)
    cosC = round(a * a + b * b - c * c, 6) / round(2 * a * b, 10)

    A = math.degrees(math.acos(cosA))
    B = math.degrees(math.acos(cosB))
    C = math.degrees(math.acos(cosC))

    S = 0.5 * a * c * math.sin(math.radians(B))
    r = 2 * S / (a + b + c)

    tanA4 = round(math.tan(math.radians(A) / 4), 10)
    tanB4 = round(math.tan(math.radians(B) / 4), 10)
    tanC4 = round(math.tan(math.radians(C) / 4), 10)

    r1 = ((1 + tanB4) * (1 + tanC4)) / (2 * (1 + tanA4)) * r
    r2 = ((1 + tanC4) * (1 + tanA4)) / (2 * (1 + tanB4)) * r
    r3 = ((1 + tanA4) * (1 + tanB4)) / (2 * (1 + tanC4)) * r

    print(r1, r2, r3)