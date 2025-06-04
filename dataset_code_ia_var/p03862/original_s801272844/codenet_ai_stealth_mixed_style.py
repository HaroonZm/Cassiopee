N,x=map(int,input().split())
A=[int(s)for s in input().split()]

def build_B(a,n):
    b=[a[0]]
    for j in range(n-1):b.append(a[j]+a[j+1])
    b.append(a[-1])
    return b
B=build_B(A,N)

ans=0
i=0
while i<N+1:
    b=B[i]
    if b>x:
        diff=b-x
        ans=ans+diff
        B[i]-=diff
        if i!=N:
            B[i+1]=B[i+1]-diff
    i+=1
print(ans)