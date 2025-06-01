n,k=map(int,raw_input().split())
a=[]
for i in range(n+k):
    a.append(input())
c=[]
for i in range(n):
    c.append(0)
for i in range(n,n+k):
    for j in range(n):
        if a[i]>=a[j]:
            c[j]+=1
            break
max_val=c[0]
max_idx=0
for i in range(1,n):
    if c[i]>max_val:
        max_val=c[i]
        max_idx=i
print max_idx+1