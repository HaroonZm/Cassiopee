n,a,b=map(int,input().split())
if n==1 and a!=b:
    print(0)
    exit()
if a>b:
    print(0)
    exit()
mi=(n-1)*a+b
ma=(n-1)*b+a
print(ma-mi+1)