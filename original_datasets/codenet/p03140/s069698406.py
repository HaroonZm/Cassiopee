import collections
n=int(input())
a=input()
b=input()
c=input()

ans=0

for i in range(n):
    x=[a[i],b[i],c[i]]
    d=collections.Counter(x)
    ans+=len(d)-1

print(ans)