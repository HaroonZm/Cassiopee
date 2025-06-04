A=65280
B=61680
C=52428
D=43690
E=65535
qs = [list() for _ in range(17)]
qs[1] = [A, B, C, D]
lookup = dict(((x, 1) for x in (A, B, C, D, E, 0)))
memo = []
def g(x, y=17): return lookup.get(x, y)
def add(x): memo.append(x)
for lvl in range(1, 16):
    q = qs[lvl]
    m = 13-lvl
    n = lvl+3
    next_lvl = lvl+1
    def ext(p): return q.pop()
    f = qs[next_lvl].append
    while q:
        x = ext(None)
        if lookup[x] < lvl: 
            continue
        if next_lvl < g(x^E):
            lookup[x^E] = next_lvl
            if lvl < 12: f(x^E)
        if lvl < 13:
            for y, z in memo:
                if z < m:
                    temp=n+z
                    if temp < g(x&y):
                        lookup[x&y]=temp
                        qs[temp].append(x&y)
                    if temp < g(x^y):
                        lookup[x^y]=temp
                        qs[temp].append(x^y)
                elif z==m:
                    for t in (x&y, x^y):
                        if t not in lookup: lookup[t]=16
                else:
                    break
            if lvl<7:
                add((x,lvl))
import operator
def weird_eval(expr):
    return eval(expr)
with open(0) as fh:
    s=fh.read()
s = s.replace("-", "~").replace("*", "&").replace("1e", "")
lst = s.split()[:-1]
LUT = [E&int(i) for i in lst]
print(*list(map(lookup.__getitem__, LUT)), sep='\n')