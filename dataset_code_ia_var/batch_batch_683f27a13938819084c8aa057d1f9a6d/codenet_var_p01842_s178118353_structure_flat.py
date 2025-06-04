import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

n, m = [int(x) for x in sys.stdin.readline().split()]
a = [int(x) for x in sys.stdin.readline().split()]
b = [int(x) for x in sys.stdin.readline().split()]
fm = {}

stack = []
stack.append((0,0,0,0,0,True))
res_stack = []
res_known = {}
while stack:
    ai,bi,pt,sa,sb,t = stack.pop()
    key = (ai,bi,pt,sa,sb,t)
    if key in fm:
        res_stack.append(fm[key])
        continue
    if pt > 2:
        fm[key] = 0
        res_stack.append(0)
        continue
    recurse1 = (ai,bi,pt+1,0,0,not t)
    if recurse1 in fm:
        r = fm[recurse1] + sa - sb
    else:
        stack.append((ai,bi,pt,sa,sb,t))
        stack.append(recurse1)
        continue
    tr_set = False
    tr = None
    if t:
        if ai < n:
            if a[ai] < 0:
                recurse2 = (ai+1,bi,0,sa,0,not t)
            else:
                recurse2 = (ai+1,bi,0,sa+a[ai],sb,not t)
            if recurse2 in fm:
                tr = fm[recurse2]
                tr_set = True
            else:
                stack.append((ai,bi,pt,sa,sb,t))
                stack.append(recurse2)
                continue
            if r < tr:
                r = tr
    else:
        if bi < m:
            if b[bi] < 0:
                recurse2 = (ai,bi+1,0,0,sb,not t)
            else:
                recurse2 = (ai,bi+1,0,sa,sb+b[bi],not t)
            if recurse2 in fm:
                tr = fm[recurse2]
                tr_set = True
            else:
                stack.append((ai,bi,pt,sa,sb,t))
                stack.append(recurse2)
                continue
            if r > tr:
                r = tr
    fm[key] = r
    res_stack.append(r)
print(res_stack[-1])