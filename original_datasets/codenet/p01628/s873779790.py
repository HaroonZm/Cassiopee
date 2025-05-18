from itertools import permutations
N,M=map(int,input().split())
k=[int(input())-1 for i in range(M)]
g=[i for i in range(N)]
for i in range(N):
    for j in k:
        if g[i]==j:
            g[i]=j+1
        elif g[i]==j+1:
            g[i]=j
s=10
for K in permutations(k):
    G=[i for i in range(N)]
    for i in range(N):
        for j in K:
            if G[i]==j:
                G[i]=j+1
            elif G[i]==j+1:
                G[i]=j
    if G!=g:
        continue

    l=[0]*N
    for i in range(M):
        a=K[i]
        b=max(l[a],l[a+1])
        l[a]=b+1
        l[a+1]=b+1
    s=min(s,max(l))
print(s)