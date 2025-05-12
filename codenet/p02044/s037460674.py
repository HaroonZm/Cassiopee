while True:
    n,m=map(int,input().split())
    if (n,m)==(0,0):
        break
    t=m//n
    a=list(map(int,input().split()))
    cnt=0
    for i in a:
        if t<=i:
            cnt+=t
        else:
            cnt+=i
    print(cnt)