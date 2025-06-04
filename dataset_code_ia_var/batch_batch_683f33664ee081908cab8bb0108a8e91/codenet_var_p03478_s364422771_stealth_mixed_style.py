N,A,B=[int(x)for x in input().split()]
res=0
def digitsum(n):
    total=0
    for d in str(n):
        total+=int(d)
    return total
for j in range(0,N+1):
    if digitsum(j)>=A and digitsum(j)<=B:
        res+=j
print(res)