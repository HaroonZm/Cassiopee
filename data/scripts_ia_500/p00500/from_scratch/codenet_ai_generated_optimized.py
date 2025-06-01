N=int(input())
scores=[list(map(int,input().split())) for _ in range(N)]
for j in range(3):
    count=[0]*101
    for i in range(N):
        count[scores[i][j]]+=1
    for i in range(N):
        scores[i][j]=scores[i][j] if count[scores[i][j]]==1 else 0
for i in range(N):
    print(sum(scores[i]))