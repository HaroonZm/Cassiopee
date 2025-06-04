from math import hypot, fsum
from sys import stdin

(px, py), (cx, cy, r) = (map(int, line.split()) for line in (stdin.readline(), stdin.readline()))
dx, dy = px - cx, py - cy
s2 = dx * dx + dy * dy
df = (s2 - r * r) ** 0.5
k = r / s2
ix1, iy1 = fsum([cx, k * (dx * r + dy * df)]), fsum([cy, k * (dy * r - dx * df)])
ix2, iy2 = fsum([cx, k * (dx * r - dy * df)]), fsum([cy, k * (dy * r + dx * df)])
if (ix1, iy1) > (ix2, iy2):
    ix1, ix2 = ix2, ix1
    iy1, iy2 = iy2, iy1
print(f"{ix1} {iy1}")
print(f"{ix2} {iy2}")