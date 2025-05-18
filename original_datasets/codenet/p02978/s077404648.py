N=int(input())
A=list(map(int,input().split()))

memo={}
def dp(i,j,L,R):
    if (i,j,L,R) in memo:
        return memo[(i,j,L,R)]
    if i==j:
        memo[(i,j,L,R)]=0
        memo[(i,j,L,R)]=(L+R)*A[i]
        return (L+R)*A[i]
    elif i>j:
        return 0

    ans=10**18
    for k in range(i,j+1):
        test=dp(i,k-1,L,L+R)+dp(k+1,j,L+R,R)+A[k]*(L+R)
        ans=min(ans,test)

    memo[(i,j,L,R)]=0
    memo[(i,j,L,R)]=ans
    return ans

res=dp(1,N-2,1,1)
print(res+A[0]+A[-1])