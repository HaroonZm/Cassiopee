def x():
    m=-10**9
    for i in N:
        p=[0]*n
        for j in range(i,n):
            for k in N:
                p[k]+=l[k][j]
            m=max(P(p),m)
    return m

def P(a):
    m,c=-10**5,0
    for x in N:
        c+=a[x]
        m=max(c,m)
        if c<0:
            c=0
    return m

n=int(raw_input())
N=range(n)
l=[]
for i in N:
    l.append(map(int,raw_input().split()))
print x()