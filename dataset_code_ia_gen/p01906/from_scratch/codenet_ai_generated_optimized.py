N,M=map(int,input().split())
A=list(map(int,input().split()))
G=N//g=GCD=1
def gcd(a,b):
    while b:b,a=b,a%b
    return a
g=gcd(N,M)
G=N//g
res=0
for shift in range(G):
    vals=[A[(shift+i)%N] for i in range(M)]
    res+=max(vals)-min(vals)
print(res)