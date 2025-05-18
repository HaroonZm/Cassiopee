n=int(input())
a=list(map(int,input().split()))
for i in range(1,n+1):
    if n%i==0:
        for j in range(n):
            if j>=i and a[j]!=a[j-i]:break
        else:print(n//i);exit()
print(1)