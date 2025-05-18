n,m,c=list(map(int,input().split()))
b=list(map(int,input().split()))
a=[]
for i in range(n):
    a1=list(map(int,input().split()))
    a.append(a1)

sum=0
for i in range(n):
    t=0
    for j in range(m):
       t+=a[i][j]*b[j]
    t+=c
    if t>0:
        sum+=1
print(sum)