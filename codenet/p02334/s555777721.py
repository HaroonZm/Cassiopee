n,k=map(int,input().split(" "))
a=1
for i in range(k,n+k):
    a*=i
for i in range(1,n+1):
    a//=i
print(a%(10**9+7))