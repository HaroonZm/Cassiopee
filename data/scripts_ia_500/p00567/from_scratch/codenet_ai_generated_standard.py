N=int(input())
L=[int(input()) for _ in range(N)]
psum=[0]
for x in L:
    psum.append(psum[-1]+x)
res=10**9
for i in range(1, N):
    for j in range(i+1, N+1):
        pieces=[psum[i]-psum[0], psum[j]-psum[i], psum[-1]-psum[j]]
        diff=max(pieces)-min(pieces)
        if diff<res:
            res=diff
print(res)