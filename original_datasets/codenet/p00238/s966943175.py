while 1:
    a=int(input())
    if a == 0: break
    b=int(input())
    for _ in range(b):
        c=list(map(int,input().split()))
        a-=c[1]-c[0]
    print(a if a>0 else 'OK')