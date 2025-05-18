import sys

def Integral(x):
    return x**2

def test(d):
    s=0
    n=int(600/d)
    for i in range(1,n):
        s+=Integral(d*i)*d
    return s

for d in sys.stdin:
    d=int(d)
    print(test(d))