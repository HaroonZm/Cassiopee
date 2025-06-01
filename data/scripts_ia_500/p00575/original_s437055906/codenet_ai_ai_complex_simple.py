from functools import reduce
A,B,C=map(int,input().split())
f=lambda x,y: (x//y, x%y)
g=lambda a,b,c:(c//(7*a+b), c%(7*a+b))
h=lambda k,a,b,c:print(7*k+(c+a-1)//a) if c<=7*a else print(7*(k+1))
t=g(A,B,C)
h(*t,A,B,C)