import itertools
N,M=map(int,input().split())
branch=[]
for _ in range(M):
    a,b=map(int,input().split())
    branch.append([a,b])
    branch.append([b,a])
ans=0
for perm in itertools.permutations(list(range(1,N+1))):
    f=True
    if perm[0]==1:
        for i in range(N-1):
            if not [perm[i],perm[i+1]] in branch:
                f=False
        if f:
            ans+=1
print(ans)