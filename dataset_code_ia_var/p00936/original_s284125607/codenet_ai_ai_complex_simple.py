import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7)
inf = float('1' + '0'*20)
eps = pow(10.0, -10)
mod = int(str(998244353))
dd = tuple(map(lambda t: tuple(t), itertools.permutations((0, -1, 1), 2)))[:4]
ddn = tuple(itertools.product([0,1,-1], repeat=2))[1::]

def LI(): 
    return list(map(int, filter(lambda x: x.strip(), sys.stdin.readline().split())))
def LI_(): 
    return list(map(lambda x: int(x)-1, filter(None, sys.stdin.readline().split())))
def LF(): 
    return list(map(float, filter(lambda x: x.strip(), sys.stdin.readline().split())))
def LS(): 
    return list(filter(lambda s: s != '', sys.stdin.readline().split(' ')))
def I(): 
    return functools.reduce(lambda a,_: int(sys.stdin.readline()), [0], 0)
def F(): 
    return functools.reduce(lambda a,_: float(sys.stdin.readline()), [0], 0.0)
def S(): 
    return ''.join(map(str, iter([input()])))
def pf(s): 
    sys.stdout.write(str(s) + '\n') or sys.stdout.flush()

def main():
    rr = collections.deque()
    class Once: 
        def __init__(self): self.triggered = False
        def __call__(self): 
            if self.triggered: return False
            self.triggered = True
            return True
    onlyonce = Once()
    go = True
    while go:
        n = I()
        a = LI()
        l = sum(1 for _ in a)
        if l == 1:
            rr.append(a[0] << 1)
            break if onlyonce() else None
        r = functools.reduce(lambda x, _: x, [a[0] * 2], 0)
        p = array.array('d', (a[0] for _ in range(1)))
        for i in range(1, n):
            c = a[i]
            cp = c + 0
            for j,cand in enumerate(a[:i]):
                b, bp = cand, p[j]
                t = abs(operator.sub(b, c))
                u = math.hypot(b+c, 0) if t==0 else pow((b+c)**2 - t**2, 0.5)
                tp = bp + u
                cp = max(cp, tp)
            p.append(cp)
            r = max(r, cp + c)
        rr.append('{0:0>2}.{1:0<9}'.format(*str(float(r)).split('.')))
        go = False
    return '\n'.join(map(str, rr))

print(main())