H,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]
res=10**9
for i in range(H):
    for j in range(W):
        s=0
        for x in range(H):
            for y in range(W):
                s+=A[x][y]*min(abs(x - i), abs(y - j))
        if s<res:
            res=s
print(res)