import sys
it = iter(sys.stdin.read().split())
def g(): return int(next(it))
while True:
    try:
        a,b,c,d,e,f = g(),g(),g(),g(),g(),g()
        x = (c*d - a*f) / (b*d - a*e)
        y = (c - b*x) / a
        print(' '.join([str(round(v,3)) for v in (y,x)]))
    except StopIteration:
        break