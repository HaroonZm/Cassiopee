h,w,k=map(int, input().split())
s=[list(input()) for _ in range(h)]

ans=[[0]*w for i in range(h)]
cnt=1
for i in range(h):
    for j in range(w):
        if s[i][j]=="#":
            ans[i][j]=cnt
            cnt+=1

for i in range(h):
    for j in range(w):
        if ans[i][j]==0:
            if j!=0:
                ans[i][j]=ans[i][j-1]
for i in range(h):
    for j in range(w-1, -1, -1):
        if ans[i][j]==0:
            if j!=(w-1):
                ans[i][j]=ans[i][j+1]

# for i in range(h):
#     print(*ans[i])
# print()

for i in range(h):
    for j in range(w):
        if ans[i][j]==0:
            if i!=0:
                ans[i][j]=ans[i-1][j]

for i in range(h-1, -1, -1):
    for j in range(w):
        if ans[i][j]==0:
            if i!=(h-1):
                ans[i][j]=ans[i+1][j]

for i in range(h):
    print(*ans[i])