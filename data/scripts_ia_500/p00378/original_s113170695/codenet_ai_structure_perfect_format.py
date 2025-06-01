A,B,X=map(int,input().split())
k=X//1000
ans=k*min(A,2*B)
r=X-1000*k
if 0<r<=500:
    ans+=min(A,B)
elif r>500:
    ans+=min(A,2*B)
print(ans)