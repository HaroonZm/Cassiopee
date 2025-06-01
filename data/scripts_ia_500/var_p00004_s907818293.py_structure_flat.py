import sys
for line in sys.stdin:
    a,b,c,d,e,f = [int(x) for x in line.split()]
    denom = a*e - b*d
    x = (c*e - b*f) / denom
    y = (a*f - c*d) / denom
    print("%.3f %.3f" % (x, y))