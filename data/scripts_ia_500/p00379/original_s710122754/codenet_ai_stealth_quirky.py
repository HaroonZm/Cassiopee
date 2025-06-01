_ = []
a,n,s = map(int,input().split())
ans = []
for i in range(1,10**4+1):
    if i**n <= s:
        _.append(i**n)
for i in _:
    d = a
    for j in str(i):
        d += int(j)
    if d**n == i:
        ans+=[i]
print(len(ans))