import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

nuvm = sys.stdin.readline().split()
n = int(nuvm[0])
u = int(nuvm[1])
v = int(nuvm[2])
m = int(nuvm[3])
ud = {}
i = 0
while i < n:
    t = [int(x) for x in sys.stdin.readline().split()]
    j = 0
    while j < n:
        ud[t[j]] = (i,j)
        j += 1
    i += 1
vd = {}
i = 0
while i < n:
    t = [int(x) for x in sys.stdin.readline().split()]
    j = 0
    while j < n:
        vd[t[j]] = (i,j)
        j += 1
    i += 1
ma = []
count_m = 0
while count_m < m:
    ma.append(int(sys.stdin.readline()))
    count_m += 1
ut = collections.defaultdict(bool)
vt = collections.defaultdict(bool)
un = 0
vn = 0
idx = 0
draw_flag = False
while idx < len(ma):
    t = ma[idx]
    if t in ud:
        ut[ud[t]] = True
        ui, uj = ud[t]
        didx = 0
        while didx < 4:
            di, dj = ddn[didx]
            k = 1
            i1 = 1
            while i1 < n:
                if not ut[(ui+di*i1, uj+dj*i1)]:
                    break
                k += 1
                i1 += 1
            i2 = -1
            count = 1
            while count < n:
                if not ut[(ui+di*i2, uj+dj*i2)]:
                    break
                k += 1
                i2 -= 1
                count += 1
            if k >= n:
                un += 1
                if k == 1:
                    un = 1
            didx += 1
    if t in vd:
        vt[vd[t]] = True
        vi, vj = vd[t]
        didx = 0
        while didx < 4:
            di, dj = ddn[didx]
            k = 1
            i1 = 1
            while i1 < n:
                if not vt[(vi+di*i1, vj+dj*i1)]:
                    break
                k += 1
                i1 += 1
            i2 = -1
            count = 1
            while count < n:
                if not vt[(vi+di*i2, vj+dj*i2)]:
                    break
                k += 1
                i2 -= 1
                count += 1
            if k >= n:
                vn += 1
                if k == 1:
                    vn = 1
            didx += 1
    if un >= u and vn < v:
        print("USAGI")
        sys.exit()
    if vn >= v and un < u:
        print("NEKO")
        sys.exit()
    if un >= u and vn >= v:
        draw_flag = True
        break
    idx += 1
print("DRAW")