import math
import sys

def max_area(a, l, x):
    h = math.sqrt(l**2 - (a/2)**2)
    def area(t):
        # t: length from l to l+x used on one side
        s = l + x
        d = t
        e = s - t
        # height of original triangle
        H = h
        # length of base AB
        A = a
        # area of original triangle
        area_ABC = A * H / 2
        # area of added triangles from "detached" parts: base * height / 2
        # The height for added triangles is under the assumption of isosceles or from length and similar triangles properties
        # Compute height for triangle ADC with side AD = d, base AC = l
        h_d = math.sqrt(d**2 - (a/2)**2) if d > a/2 else 0
        # Compute height for triangle BEC with side BE = e, base BC = l
        h_e = math.sqrt(e**2 - (a/2)**2) if e > a/2 else 0
        return area_ABC + (a * (h_d + h_e)) / 2

    left, right = l, l + x
    for _ in range(50):
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        if area(m1) < area(m2):
            left = m1
        else:
            right = m2
    return area((left + right) / 2)

for line in sys.stdin:
    if not line.strip():
        continue
    a, l, x = map(int, line.split())
    print(f"{max_area(a, l, x):.10f}")