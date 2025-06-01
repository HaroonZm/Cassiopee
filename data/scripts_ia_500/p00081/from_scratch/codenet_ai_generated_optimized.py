import sys
for line in sys.stdin:
    if not line.strip():
        continue
    x1,y1,x2,y2,xq,yq = map(float,line.strip().split(','))
    dx,dy = x2 - x1, y2 - y1
    t = ((xq - x1)*dx + (yq - y1)*dy) / (dx*dx + dy*dy)
    xp, yp = x1 + t*dx, y1 + t*dy
    xr, yr = 2*xp - xq, 2*yp - yq
    print(f"{xr:.6f} {yr:.6f}")