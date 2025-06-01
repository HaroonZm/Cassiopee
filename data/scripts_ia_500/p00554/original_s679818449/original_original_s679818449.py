n,m=map(int,input().split())
p=[]
for i in range(m):
    p.append(list(map(int,input().split())))
p.sort()
p.pop(0)
ans=0
for i in p:
    if i[0]<n:ans+=i[1]-n
    else:break
print(ans)