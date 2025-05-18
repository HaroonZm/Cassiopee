import sys
for s in sys.stdin:
    a,b,c,d,e,f,g,h=map(float,s.split())
    if abs((c-a)*(g-e)+(d-b)*(h-f))<1e-10:m="YES"
    else:m="NO"
    print m