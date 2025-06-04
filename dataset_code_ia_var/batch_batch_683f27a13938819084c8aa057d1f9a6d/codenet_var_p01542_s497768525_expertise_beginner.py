import sys
import itertools

sys.setrecursionlimit(10000000)

inf = 10**20
mod = 10**9 + 7

dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    print(s, flush=True)

def main():
    rr = []
    def f(s):
        ca = '01+-*()'
        sa = s.split('.')
        r = -1
        sl = len(sa)
        fm = {}

        def _f(s):
            if s in fm:
                return fm[s]
            if ')' in s:
                ri = s.index(')')
                if len(s) > ri+1 and s[ri+1] in '01':
                    fm[s] = -1
                    return -1
                li = -1
                for i in range(ri-1,-1,-1):
                    if s[i] == '(':
                        li = i
                        break
                if li < 0 or (li > 0 and s[li-1] in '01'):
                    fm[s] = -1
                    return -1
                ts = s[li+1:ri]
                if ('+' not in ts and '-' not in ts and '*' not in ts):
                    fm[s] = -1
                    return -1
                tr = _f(ts)
                if tr == -1:
                    fm[s] = -1
                    return -1
                fm[s] = _f(s[:li] + tr + s[ri+1:])
                return fm[s]
            if '(' in s:
                fm[s] = -1
                return -1
            l = len(s)
            if '*' in s:
                oi = s.index('*')
                li = oi
                for i in range(oi-1,-1,-1):
                    if s[i] not in '01':
                        break
                    li = i
                ri = oi
                for i in range(oi+1,l):
                    if s[i] not in '01':
                        break
                    ri = i
                if li == oi or ri == oi:
                    fm[s] = -1
                    return -1
                try:
                    t = int(s[li:oi], 2)
                    u = int(s[oi+1:ri+1], 2)
                except:
                    fm[s] = -1
                    return -1
                tu = t * u
                if t < 0 or t >= 1024 or u < 0 or u >= 1024 or tu < 0 or tu >= 1024:
                    fm[s] = -1
                    return -1
                ts = bin(tu)[2:]
                fm[s] = _f(s[:li] + ts + s[ri+1:])
                return fm[s]
            pi = inf
            mi = inf
            if '+' in s:
                pi = s.index('+')
            if '-' in s:
                mi = s.index('-')
            if pi == inf and mi == inf:
                try:
                    t = int(s,2)
                except:
                    fm[s] = -1
                    return -1
                fm[s] = s
                if t < 0 or t >= 1024:
                    fm[s] = -1
                return fm[s]
            oi = min(pi, mi)
            li = oi
            for i in range(oi-1,-1,-1):
                if s[i] not in '01':
                    break
                li = i
            ri = oi
            for i in range(oi+1,l):
                if s[i] not in '01':
                    break
                ri = i
            if li == oi or ri == oi:
                fm[s] = -1
                return -1
            try:
                t = int(s[li:oi],2)
                u = int(s[oi+1:ri+1],2)
            except:
                fm[s] = -1
                return -1
            tu = t + u
            if oi == mi:
                tu = t - u
            if t < 0 or t >= 1024 or u < 0 or u >= 1024 or tu < 0 or tu >= 1024:
                fm[s] = -1
                return -1
            ts = bin(tu)[2:]
            fm[s] = _f(s[:li] + ts + s[ri+1:])
            return fm[s]

        for comb in itertools.product(ca, repeat=sl-1):
            t = ''
            for i in range(len(comb)):
                t += sa[i]
                t += comb[i]
            t += sa[-1]
            tr = _f(t)
            if tr != -1:
                try:
                    val = int(tr,2)
                except:
                    val = -1
                if val >= 1024 or val < 0:
                    val = -1
                if r < val:
                    r = val
        return r

    while True:
        n = S()
        if n == "0":
            break
        rr.append(f(n))
        break

    return '\n'.join([str(x) for x in rr])

print(main())