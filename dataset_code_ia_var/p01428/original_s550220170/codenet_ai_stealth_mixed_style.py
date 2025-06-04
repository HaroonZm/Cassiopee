mp = []
for i in range(10):
    if i == 0 or i == 9:
        mp.append(list("X"*10))
    else:
        row = input()
        mp.append(['X'] + [c for c in row] + ['X'])

vecs = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]

def search(a,b,x,y,dx,dy):
    count = 0; nx = x+dx; ny = y+dy
    while True:
        if mp[ny][nx]==b: nx+=dx; ny+=dy; count+=1
        else: break
    return count if mp[ny][nx]==a else 0

def score(a,b,x,y):
    return sum(search(a,b,x,y,dx,dy) for dx,dy in vecs)

def locate(a,b,x,y):
    mp[y][x]=a
    for _vec in vecs:
        result=search(a,b,x,y,*_vec)
        if result:
            nx,ny=x+_vec[0],y+_vec[1]
            while mp[ny][nx]==b:
                mp[ny][nx]=a
                nx+=_vec[0]; ny+=_vec[1]

def temp(a,b,desc):
    s,mx,my=0,-1,-1
    r=(range(1,9) if desc else range(8,0,-1))
    for y in r:
        for x in r:
            if mp[y][x]!='.': continue
            t=score(a,b,x,y)
            if t>s:
                mx,my,s=x,y,t
    if s:
        locate(a,b,mx,my)
        return True
    return 0

mami = lambda: temp('o','x',1)
def witch(): return temp('x','o',0)

def play():
    while 1:
        f=0
        for func in (mami,witch):
            f=func() or f
        if not f: break

play()
for l in mp[1:9]: print("".join(l[1:9]))