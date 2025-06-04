K,N=[int(x) for x in input().split()]
A=list(map(int,input().split()))
def get_diff(a,n,k):
    res=[]
    for idx in range(n-1):
        res+=[a[idx+1]-a[idx]]
    res.append(a[0]+k-a[-1])
    return res
B=[]
for j in range(N):
    if j!=N-1:
        B.append(A[j+1]-A[j])
B.extend([A[0]+K-A[N-1]]) if B else None
max_diff = 0
for x in range(len(B)):
    if B[x]>max_diff:
        max_diff=B[x]
print(K-max_diff)