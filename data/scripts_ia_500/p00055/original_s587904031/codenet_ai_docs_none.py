import sys
for x in sys.stdin:
    s=0
    a=float(x)
    for i in range(10):
        s+=a
        if i%2==0:
            a*=2
        else:
            a/=3
    print(s)