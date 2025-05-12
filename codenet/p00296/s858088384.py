n,_,_=map(int,input().split())
a,b=list(range(n)),0
for i in map(int,input().split()):
    b-= i if i&1 else -i
    b%=n
    del a[b]
    n-=1
for i in map(int,input().split()):
    print(int(i in a))