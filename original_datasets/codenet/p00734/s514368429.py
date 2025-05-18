def f():
    for i in t:
        for j in h:
            if (i-j)*2==sumt-sumh:
                print(i,j)
                return
    print(-1)
            

while True:
    n,m=map(int,input().split())
    if n==0:
        break
    t=[int(input()) for i in range(n)]
    h=[int(input()) for j in range(m)]
    t.sort()
    h.sort()
    sumt=sum(t)
    sumh=sum(h)
    f()