a,n,m=map(int,input().split())
candi=[]
ans=0
for i in range((lambda x,y:x+y)(a+1,72)):
    ipow=i**n
    if ipow<=m:candi+=[ipow]
for j in candi:
    k,digit=j,[]
    for __ in range(9):digit+=[k%10];k//=10
    if (sum(digit)+a)**n==j:ans+=1
print(ans)