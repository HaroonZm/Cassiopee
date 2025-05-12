a,b,c,d  = map(int,input().split())
x,y,z,w  = map(int,input().split())

A = a+b+c+d
B = x+y+z+w

print(max(A,B))