import sys
eps = 1e-10
for line in sys.stdin:
    if not line.strip():
        continue
    xA,yA,xB,yB,xC,yC,xD,yD = map(float,line.split())
    vx1, vy1 = xB - xA, yB - yA
    vx2, vy2 = xD - xC, yD - yC
    dot = vx1*vx2 + vy1*vy2
    print("YES" if abs(dot) < eps else "NO")