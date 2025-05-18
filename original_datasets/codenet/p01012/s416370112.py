m,n,x=[int(i) for i in input().split()]
k,l,y=[int(i) for i in input().split()]

res=0.5*(1.0+((m**2+n**2)**x)/((m+n)**(2*x)))
res*=0.5*(1.0+((k**2+l**2)**y)/((k+l)**(2*y)))
print(res)