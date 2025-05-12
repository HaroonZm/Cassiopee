while True:
    n=input()
    if n==0:break
    L=[input() for i in range(n)]
    v=input()
    l,r=0,len(L)-1
    cnt=0
    while l<=r:
        m=(l+r)/2
        if L[m]==v:
            print cnt+1
            break
        elif L[m]<v:
            l=m+1
        elif L[m]>v:
            r=m-1
        cnt+=1
    else:
        print cnt