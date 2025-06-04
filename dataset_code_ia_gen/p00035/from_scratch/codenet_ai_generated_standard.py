import sys

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

for line in sys.stdin:
    if not line.strip():
        continue
    vals = line.strip().split(',')
    A = (float(vals[0]), float(vals[1]))
    B = (float(vals[2]), float(vals[3]))
    C = (float(vals[4]), float(vals[5]))
    D = (float(vals[6]), float(vals[7]))
    pts = [A, B, C, D]
    crosses = []
    for i in range(4):
        o = pts[i]
        a = pts[(i+1)%4]
        b = pts[(i+2)%4]
        c = cross(o,a,b)
        crosses.append(c)
    pos = sum(1 for x in crosses if x>0)
    neg = sum(1 for x in crosses if x<0)
    print("YES" if pos==4 or neg==4 else "NO")