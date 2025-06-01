n,*_=map(int,input().split())
a= list(range(n))
b=0
for i in map(int,input().split()):
    b=(b - i if i&1 else b + i) % len(a)
    a.pop(b)
for i in map(int,input().split()):
    print(i in a)