path=[list(map(int,input().split())) for i in range(0,3)]

cnt=[0,0,0,0]

for i in range(0,3):
    for j in range(0,2):
        cnt[path[i][j]-1]+=1

if cnt[0]<3 and cnt[1]<3 and cnt[2]<3 and cnt[3]<3:
    print("YES")
else:
    print("NO")