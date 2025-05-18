n, m=map(int, input().split())
cake=[list(map(int, input().split())) for _ in range(n)]

cakes=[[] for _ in range(8)]
for c in cake:
    cakes[0].append(c[0]+c[1]+c[2])
    cakes[1].append(c[0]+c[1]-c[2])
    cakes[2].append(c[0]-c[1]+c[2])
    cakes[3].append(c[0]-c[1]-c[2])
    cakes[4].append(-c[0]+c[1]+c[2])
    cakes[5].append(-c[0]+c[1]-c[2])
    cakes[6].append(-c[0]-c[1]+c[2])
    cakes[7].append(-c[0]-c[1]-c[2])
for c in cakes:
    c.sort(reverse=True)
ans=0
for i in range(8):
    ans=max(ans, sum(cakes[i][:m]))
print(ans)