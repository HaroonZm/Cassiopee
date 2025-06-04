px, py = map(int, input().split())
cx, cy, r = map(int, input().split())
dx = px - cx
dy = py - cy
s2 = dx ** 2 + dy ** 2
df = (s2 - r ** 2) ** 0.5
ix1 = (dx * r + dy * df) * r / s2
ix2 = (dx * r - dy * df) * r / s2
iy1 = (dy * r - dx * df) * r / s2
iy2 = (dy * r + dx * df) * r / s2
if (ix1, iy1) > (ix2, iy2):
    ix1, ix2 = ix2, ix1
    iy1, iy2 = iy2, iy1
print(ix1 + cx, iy1 + cy)
print(ix2 + cx, iy2 + cy)