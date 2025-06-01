i=0
while 1:
    try: n=int(input())
    except: break
    if not n: break
    y=float(input())
    id_,vmax=-1,-float('inf')
    while i<n:
        b,r,t=*map(int,input().split()),
        if t==1: m=y*(r/100)+1
        else: m=(1+r/100)**y
        id_,vmax=(b,m) if id_<0 or m>=vmax else (id_,vmax)
        i+=1
    print(id_)
    i=0