m=998244353
M=1<<20
f=[0]*M
g=[0]*M
h=[0]*M
f[0]=g[0]=f[1]=g[1]=h[1]=1
for i in range(2,M):
	f[i]=f[i-1]*i%m
	h[i]=m-h[m%i]*(m//i)%m
	g[i]=g[i-1]*h[i]%m
A,B=map(int,input().split())
if A<B:A,B=B,A
a=0
b=1
for j in range(1,B+1):
	a+=b*f[A+B-j]*g[B-j]*g[A]
	b=b*2%m
print((a*f[A]*f[B]*g[A+B]+A)%m)