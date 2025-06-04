while True:
    n,m,a=map(int,input().split())
    if n==0 and m==0 and a==0:
        break
    lines=[]
    for _ in range(m):
        h,p,q=map(int,input().split())
        lines.append((h,p,q))
    lines.sort(reverse=True)
    pos=a
    for _,p,q in lines:
        if pos==p:
            pos=q
        elif pos==q:
            pos=p
    print(pos)