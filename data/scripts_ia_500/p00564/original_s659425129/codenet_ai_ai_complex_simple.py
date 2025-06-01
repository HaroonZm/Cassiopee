from math import ceil as c
N,A,B,C,D=map(int,input().split())
f=lambda n,a,b:c(n/a)*b
x,y=(lambda u,v:(u,v) if u<v else (v,u))(f(N,A,B),f(N,C,D))
exec("print(x)") if x==y else print(x if x<y else y)