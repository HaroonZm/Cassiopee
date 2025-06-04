import sys
sys.setrecursionlimit(10**7)
N=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))

pos = [0]*(N+1)
for i,x in enumerate(a):
    pos[x]=i

# On veut vérifier si f est injective
# Si f(a_i)=f(a_j) avec i != j alors on peut construire g,h telles que g(f(x))=h(f(x)) mais g(x)!=h(x)
# Si f est injective => condition True => print Yes
# Sinon => condition False => construire g,h

inv = {}
for i,x in enumerate(b):
    if x in inv:
        inv[x].append(i)
    else:
        inv[x] = [i]

for x,idxs in inv.items():
    if len(idxs)>1:
        # Trouvé collision
        c=[0]*N
        d=[0]*N
        # On choisit g,h égaux sauf sur idxs[0] et idxs[1]
        for i in range(N):
            c[i]=1
            d[i]=1
        i1=idxs[0]
        i2=idxs[1]
        c[i1]=2
        d[i1]=1
        c[i2]=1
        d[i2]=1
        print("No")
        print(*c)
        print(*d)
        sys.exit()
print("Yes")