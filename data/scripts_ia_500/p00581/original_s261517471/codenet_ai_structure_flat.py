h,w=map(int,input().split())
s=[]
for _ in range(h):
    s.append(list(input()))
ans=0
ci=[]
for _ in range(w):
    ci.append(0)
for i in range(h-1,-1,-1):
    co=0
    for j in range(w-1,-1,-1):
        if s[i][j]=='J':
            ans+=co*ci[j]
        elif s[i][j]=='O':
            co+=1
        elif s[i][j]=='I':
            ci[j]+=1
print(ans)