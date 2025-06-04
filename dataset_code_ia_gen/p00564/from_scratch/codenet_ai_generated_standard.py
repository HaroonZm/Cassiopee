N,A,B,C,D=map(int,input().split())
x=((N+A-1)//A)*B
y=((N+C-1)//C)*D
print(min(x,y))