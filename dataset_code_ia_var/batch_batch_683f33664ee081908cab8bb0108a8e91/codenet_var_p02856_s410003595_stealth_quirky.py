def x(x):return int(x)
def y(y):return [x(z)for z in y.split()]

M=x(input())
a,b=0,0

for _ in[*range(M)]:
 d,c=y(input())
 a+=d*c
 b+=c

def f(s,t):return t-1+(s-1)//9

print(f(a,b))