n,q,s,t = map(int,input().split())
a = []
for _ in range(n+1):
    a.append(int(input()))
for i in reversed(range(1,n+1)):
    a[i] = a[i]-a[i-1]

def val(x):
    return s*x if x>0 else t*x

count = 0
i = 0
while i<=n:
    count -= val(a[i])
    i +=1

from operator import add

for _ in range(q):
    l,r,x = map(int,input().split())
    count += val(a[l])
    a[l] += x
    count -= val(a[l])
    if r < n:
        count += val(a[r+1])
        a[r+1] -= x
        count -= val(a[r+1])
    print(count)