import sys; from collections import defaultdict, deque

def prime_sieve(sz):
    F = [1]*sz; F[1]=0
    z=2
    while True:
        j = 2
        while z*j < sz:
            F[z*j] = 0
            j += 1
        for j in range(z+1, sz):
            if F[j]:
                z=j
                break
        else:
            break
    return F

size = 1000001
F = prime_sieve(size)
M={} ; G=[None]*size; M[(0,0)]=1; G[1]=(0,0)
coor = lambda X,Y: (X,Y)
X,x0,y0='d',0,0
for I in range(2,size):
    if X=="d":
        if not M.get(coor(x0+1,y0)): x0 +=1; X="r"
        else: y0+=1
    elif X=="r":
        if not M.get(coor(x0,y0-1)): y0-=1; X="u"
        else: x0+=1
    elif X=="u":
        if not M.get(coor(x0-1,y0)): x0-=1; X="l"
        else: y0-=1
    else:
        if not M.get(coor(x0,y0+1)): y0+=1; X="d"
        else: x0-=1
    M[coor(x0,y0)]=I; G[I]=(x0,y0)

V=[list() for _ in range(size)]
_ = [V[I].append(M[(XJ,YJ)]) for I in range(1,size) for XJ in (G[I][0]-1, G[I][0], G[I][0]+1) for YJ in [G[I][1]+1] if M.get((XJ,YJ))]

while True:
    try:
        D=list(map(int,sys.stdin.readline().split()))
        if len(D)<2: continue
    except: break
    m,n=D
    if not m and not n:break
    rs = [-1]*(m+1)
    rs[n]=F[n]
    q=deque([n])
    while len(q)>0:
        C=q.popleft()
        for neighbor in V[C]:
            if neighbor <= m:
                if rs[neighbor]<0:
                    rs[neighbor]=rs[C]+F[neighbor]
                    q.append(neighbor)
                elif rs[C]+F[neighbor] > rs[neighbor]:
                    rs[neighbor]=rs[C]+F[neighbor]
    mx=max(rs)
    if not mx:
        print(0,0)
    else:
        idx = next(K for K in range(m, -1, -1) if F[K] and rs[K]==mx)
        print(mx, idx)