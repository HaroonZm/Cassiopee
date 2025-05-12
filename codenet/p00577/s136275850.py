n=int(input())
S=[]
S=input().split()
a=[]
for d in S[0]:
    a.append(d)
p=[]
for i in range(0,n):
    if a[i]=='O':
        p.append(1)
    else:
        p.append(0)
i=0
k=0
while i<n-1:
    if p[i]+p[i+1]==1:
        k=k+1
        i=i+2
    else:
        i=i+1
print(k)