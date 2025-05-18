while 1:
    n,m,a=map(int,input().split())
    if n==0:
        break
    dic={}
    for i in range(1,1001):
        dic[i]=[]
    for i in range(m):
        h,p,q=map(int,input().split())
        dic[h].append((p,q))
        dic[h].append((q,p))
    h=1000
    pos=a
    while h>0:
        for d in dic[h]:
            if d[0]==pos:
                pos=d[1]
                break
        h-=1
    print(pos)