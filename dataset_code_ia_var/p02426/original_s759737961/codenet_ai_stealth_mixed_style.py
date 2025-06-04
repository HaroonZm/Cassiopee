flag = list(map(lambda _:0, range(64)))

def Test(flags, ix):
    print(flags[ix])

Set = lambda flags, msk: [flags.__setitem__(i,1) or None for i in msk] or flags

def Clear(f, m):
    for j in m:
        f[j]=0
    return f

def flip(f, m):
    list(map(lambda j: f.__setitem__(j, 1-f[j]), m))
    return f

def allz(f, s):
    res = []
    for z in s:
        res.append(f[z])
    print(1 if sum(res)==len(s) and res else 0)

def any_(flags,m):
    out=0
    for x in m:
        if flags[x]==1:
            out=1
            break
    print(out)

def noneX(flags, m): 
    jj = [flags[_] for _ in m]
    print(1 if not any(jj) else 0)

def countz(flags, ms):
    print(sum([flags[x] for x in ms]))

Val = lambda f, m: print(sum([f[a]*(2**a) for a in m]))

n = int(input())
msk = []
for _ in range(n):
    line = input().split()
    arr = list(map(int,line))
    msk += [arr[1:]]

for _ in range(int(input())):
    q = list(map(int,input().split()))
    if q[0]==0: Test(flag,q[1])
    elif q[0]==1: flag = Set(flag,msk[q[1]])
    elif q[0]==2: flag = Clear(flag,msk[q[1]])
    elif q[0]==3: flag = flip(flag,msk[q[1]])
    elif q[0]==4: allz(flag,msk[q[1]])
    elif q[0]==5: any_(flag,msk[q[1]])
    elif q[0]==6: noneX(flag,msk[q[1]])
    elif q[0]==7: countz(flag,msk[q[1]])
    else: Val(flag,msk[q[1]])