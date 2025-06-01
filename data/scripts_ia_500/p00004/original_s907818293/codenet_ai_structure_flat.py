import sys
for line in sys.stdin:
    a,b,c,d,e,f = list(map(int,line.split()))
    den = a*e - b*d
    x = (c*e - b*f) / den
    y = (a*f - c*d) / den
    print(str(round(x+0.0,3)) + " " + str(round(y+0.0,3)))