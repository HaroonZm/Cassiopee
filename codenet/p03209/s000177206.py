def do(level,x):
    if x<=0:
        return 0
    if level==0:
        return 1
    res=0
    x-=1
    if x>j[level-1]:
        x-=j[level-1]+1
        res+=k[level-1]+1
    return res+do(level-1,x)

n,x=map(int,input().split())
j=[1]+[0]*50
k=[1]+[0]*50
for i in range(1,n+1):
    j[i]=j[i-1]*2+3
    k[i]=k[i-1]*2+1
res=0
print(do(n,x))