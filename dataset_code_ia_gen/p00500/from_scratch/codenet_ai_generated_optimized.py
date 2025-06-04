N=int(input())
scores=[list(map(int,input().split())) for _ in range(N)]
for j in range(3):
    count={}
    for i in range(N):
        count[scores[i][j]]=count.get(scores[i][j],0)+1
    for i in range(N):
        if count[scores[i][j]]>1:scores[i][j]=0
result=[sum(p) for p in scores]
print(*result,sep='\n')