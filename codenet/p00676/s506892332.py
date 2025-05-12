import sys
for i in sys.stdin:
    a,l,x=map(int,i.split())
    print((a*(4*l*l-a*a)**.5+2*l*((l+x)**2-l*l)**.5)/4)