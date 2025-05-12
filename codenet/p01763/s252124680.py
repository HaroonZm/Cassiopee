def extgcd(a,b):
    if b == 0:
        x = 1
        y = 0
        return a,x,y
    g,s,t = extgcd(b,a%b)
    x,y = t,s-a//b*t
    return g,x,y

def chineserem(b,m):
    r = 0
    M = 1
    for i in range(len(b)):
        g,p,q = extgcd(M,m[i])
        if (b[i]-r)%g != 0:
            return 0,-1
        tmp = (b[i]-r)//g*p%(m[i]//g)
        r += M*tmp
        M *= m[i]//g
    return r,M
n,m,d = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
r = [[int(x) for x in input().split()] for i in range(d)]
for d in range(d):
    mo = []
    b = []
    for i in range(m):
        if r[d][i] > -1:
            mo.append(a[i])
            b.append(r[d][i])
    x,M = chineserem(b,mo)
    if M < 0:
        print(-1)
        quit()
    i = (n-x)//M
    if i < 0:
        print(-1)
        quit()
    n = M*i+x
print(n)