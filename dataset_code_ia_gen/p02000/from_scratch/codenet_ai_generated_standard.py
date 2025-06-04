n=int(input())
A=list(map(int,input().split()))
B1=A[:]
B2=A[:]
res1=res2=0
for i in range(1,n,2):
    if i<n:
        if not (B1[i-1]<B1[i]>B1[i+1] if i+1<n else True):
            B1[i],B1[i+1]=B1[i+1],B1[i]
            res1+=1
for i in range(1,n,2):
    if i<n:
        if not (B2[i-1]>B2[i]<B2[i+1] if i+1<n else True):
            B2[i],B2[i+1]=B2[i+1],B2[i]
            res2+=1
print(min(res1,res2))