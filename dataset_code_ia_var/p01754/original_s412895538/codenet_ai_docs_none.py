n,p,q=map(int,input().split())
b=[0]*n
for i in range(n):b[i]=p*i+int(input())
b.sort()
a=q*p*n+p*n*~-n//2
s=0
for i in range(1,-~n):
    s+=b[n-i]
    a=max(a,p*q*(n-i)+p*(n-i)*(~-n-i)//2-p*i*(i-1)//2-p*i*(n-i)+s)
print(a)