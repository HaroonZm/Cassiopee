n,k=map(int,input().split(" "))
if n<k:
    print(0)
else:
    a=[1,0]
    for i in range(n):
        a=[0]+[a[i-1]+i*a[i] for i in range(1,len(a))]+[0]
    for i in range(1,k+1):
        a[k]*=i
    print(a[k]%(10**9+7))