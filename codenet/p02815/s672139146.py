N=int(input())
C=sorted(list(map(int,input().split())),reverse=True)
mod=10**9+7
def mpow(x,n):
    num=1
    while n > 0:
        if n&1:
            num=num*x%mod
        x=x*x%mod
        n=n>>1
    return(num)
count=0
for i, c in enumerate(C, 2):
    count += c * (i)
    count %= mod
print(count * mpow(2, N-1)*mpow(2, N-1) % mod)