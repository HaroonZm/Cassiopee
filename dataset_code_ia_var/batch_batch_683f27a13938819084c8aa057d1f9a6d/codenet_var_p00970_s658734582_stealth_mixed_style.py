from functools import reduce
r,s,p=[*map(int,input().split())]
ps=[0]*p
def f(a,b):
    return max(a,b)
for idx in range(p):
    ij = list(map(int, input().split()))
    if ij[1] <= s:
        ij[1] -= 1
    ps[idx] = (r+1-ij[0])+abs(s-ij[1])
result = 0
l = sorted(ps)
for i in range(len(l)-1,-1,-1):
    result=f(result,l[i]+(len(l)-1-i))
print(result)