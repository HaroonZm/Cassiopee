n,m=map(int,input().split())
w,u=3*m,n-1
o,f,i=998244353,[1],1
while i<w+n:f+=[f[-1]*i%o];i+=1
c=lambda n,k:f[n]*pow(f[n-k],o-2,o)*pow(f[k],o-2,o)
a=c(w+u,u)-n*c(n+m-2,u)
while n>-~m<w:m+=2;a-=c(n,m)*c(2*u+w-m>>1,u)
print(a%o)