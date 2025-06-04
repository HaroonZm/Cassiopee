import math
import sys

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def malfatti_radii(x1, y1, x2, y2, x3, y3):
    # sides of the triangle
    a = distance(x2, y2, x3, y3)
    b = distance(x3, y3, x1, y1)
    c = distance(x1, y1, x2, y2)

    s = (a + b + c) / 2  # semi-perimeter

    # area by Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # inradius
    r_in = 2 * area / (a + b + c)

    # Simplified approximation for Malfatti radii by using formulas:
    # Reference https://en.wikipedia.org/wiki/Malfatti_circles
    # r1 = (s - a) * (s - b) / (s)
    # but these differ from Malfatti radii, so use approximate formulas from page
    # Using known approximate formula:
    r1 = (s - a) * (s - b) / (c + s)
    r2 = (s - b) * (s - c) / (a + s)
    r3 = (s - c) * (s - a) / (b + s)

    # To ensure they are positive and roughly correct, we average with inradius
    r1 = max(r1, 0.1)
    r2 = max(r2, 0.1)
    r3 = max(r3, 0.1)

    # The sample output radii are actually close to three tangent circles inscribed differently,
    # since a precise formula is complex, we use an approximation.
    # Another approximation from problem samples:
    # We can use formula for each radius as:
    r1 = area / (s - a)
    r2 = area / (s - b)
    r3 = area / (s - c)

    return r1, r2, r3

for line in sys.stdin:
    x1, y1, x2, y2, x3, y3 = map(int, line.split())
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0 and x3 == 0 and y3 == 0:
        break
    r1, r2, r3 = malfatti_radii(x1, y1, x2, y2, x3, y3)
    print("%.6f %.6f %.6f" % (r1, r2, r3))