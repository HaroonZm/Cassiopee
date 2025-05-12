def root(x):
    if x == par[x]:
        return x
    par[x] = root(par[x])
    return par[x]

def unite(x,y):
    x = root(x)
    y = root(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

n = int(input())
par = [i for i in range(2**(n))]+[-2,-1]
rank = [0]*(2**(n)+2)
a = input()
x = [None]*(2**(n-1))
for i in range(2**(n-1)):
    x[i] = (a[2*i],a[2*i+1])
    if (a[2*i]==a[2*i+1] == "0"):
        par[2**(n-1)+i] = -1
    if (a[2*i]==a[2*i+1] == "1"):
        par[2**(n-1)+i] = -2
for i in range(2**(n-1)):
    for k in range(i+1,2**(n-1)):
        if x[i] == x[k]:
            unite(2**(n-1)+i,2**(n-1)+k)

for k in range(n-2,-1,-1):
    x = [None]*(2**k)
    for l in range(2**k):
        x[l] = (root(2**(k+1)+2*l),root(2**(k+1)+2*l+1))
        if  (root(2**(k+1)+2*l) == root(2**(k+1)+2*l+1)):
            unite(2**(k+1)+2*l,2**k+l)
    for i in range(2**(k)):
        for l in range(2**(k)):
            if i != l:
                if x[i] == x[l]:
                    unite(2**(k)+i,2**(k)+l)
p = list(set(par))
p.remove(-1)
p.remove(-2)
print(len(p)-1)