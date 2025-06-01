N,A,B,C,D=map(int,input().split())
x_sets=(N+A-1)//A
y_sets=(N+C-1)//C
print(min(x_sets*B,y_sets*D))