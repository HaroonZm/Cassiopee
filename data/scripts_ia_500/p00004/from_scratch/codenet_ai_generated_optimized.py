import sys

for line in sys.stdin:
    if not line.strip():
        continue
    a,b,c,d,e,f = map(float, line.split())
    det = a*e - b*d
    x = (c*e - b*f) / det
    y = (a*f - c*d) / det
    print(f"{x:.3f} {y:.3f}")