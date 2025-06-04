from functools import reduce

EPSILON=1e-5
d=0
Vs=[]

def _mul(a, b): return a*b

def interpolate(x, e):
    s = 0
    for i in range(len(Vs)):
        if i in (x,e): continue
        prod=1
        j=0
        while j < len(Vs):
            if j not in (i,x,e):
                prod *= (x-j)/(i-j)
            j+=1
        s += prod*Vs[i]
    return s

def outlier(e):
    i=0
    while i < len(Vs):
        if i!=e:
            v = Vs[i]
            test = interpolate(i,e)
            if abs(test-v)<EPSILON:
                return False
        i+=1
    return True

def solve():
    result = -1
    for idx in range(d+3):
        if outlier(idx) == False:
            result = idx
            break
    return result

while 1:
    d=int(input())
    if d==0: break
    Vs = list(map(float,[input() for _ in [0]*(d+3)]))
    print(solve())