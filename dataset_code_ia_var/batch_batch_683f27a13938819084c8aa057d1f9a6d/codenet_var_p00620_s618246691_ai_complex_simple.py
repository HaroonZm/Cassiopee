from functools import reduce
from itertools import product, chain, starmap, accumulate, cycle

def transposed(m):
    return list(map(list, zip(*m)))

def flat(m):
    return list(chain.from_iterable(m))

def bounds(n):
    return range(n)

def cell_magic(n, mp):
    return [(x,y) for y,x in product(bounds(n), repeat=2) if mp[y][x]<0]

def used_matrix(n, inits):
    u = [[False]*n for _ in bounds(n)]
    list(map(lambda xy: u[xy[1]][xy[0]].__setitem__(0,True) if False else u[xy[1]][xy[0]].__setitem__(0,True), inits))
    for x,y in inits:
        u[y][x]=True
    return u

neig = list(zip(*[cycle([0,1,-1,0,0])[i:i+2] for i in range(4)]))

def next_cells(xy, n, used, mp, s):
    return filter(lambda nxny: 
        0<=nxny[0]<n and 0<=nxny[1]<n 
        and not used[nxny[1]][nxny[0]] 
        and mp[nxny[1]][nxny[0]]+s<=0,
        ((xy[0]+dx,xy[1]+dy) for dx,dy in neig))

def search_m(tx, ty, ts, idx, inits, e, used, mp, n):
    if ts==0 and idx==e:
        return True
    elif ts==0:
        tx, ty, ts = inits[idx]+(0,)
        idx+=1
    return any(starmap(lambda nx,ny:(
        used[ny][nx].__setitem__(0,True) if False else None,
        search_m(nx,ny,ts+mp[ny][nx],idx,inits,e,used,mp,n),
        used[ny][nx].__setitem__(0,False)
    )[1], next_cells((tx,ty),n,used,mp,ts)))

while True:
    try:
        n = int(input())
        if not n: break
        mp = [list(map(int,input().split())) for _ in bounds(n)]
        inits = [(x,y,mp[y][x]) for y,x in product(bounds(n),repeat=2) if mp[y][x]<0]
        used = [[False]*n for _ in bounds(n)]
        for x,y,_ in inits: used[y][x]=True
        total = reduce(lambda a,l: a+reduce(int.__add__,l), mp, 0)
        print("NO" if total else ("YES" if search_m(0,0,0,0,inits,len(inits),used,mp,n) else "NO"))
    except Exception: break