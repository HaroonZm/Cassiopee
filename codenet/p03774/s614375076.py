n,m=map(int,input().split())
ab=[[int(i) for i in input().split()] for i in range(n)]
cd=[[int(i) for i in input().split()] for i in range(m)]
count=[0]*n
distance=[[] for i in range(n)]
for i in range(n):
    for l in range(m):
        distance[i].append(abs(ab[i][0]-cd[l][0])+abs(ab[i][1]-cd[l][1]))
for i in range(n):
    print(distance[i].index(min(distance[i]))+1)