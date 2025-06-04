import sys

for line in sys.stdin:
    if not line.strip():
        continue
    xA, yA, xB, yB, xC, yC, xD, yD = map(float, line.split())
    v1x, v1y = xB - xA, yB - yA
    v2x, v2y = xD - xC, yD - yC
    dot = v1x * v2x + v1y * v2y
    print("YES" if abs(dot) < 1e-10 else "NO")