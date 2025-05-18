while 1:
    a=int(input())
    if a == 0: break
    b=int(input())
    d=0
    for _ in range(b):
        c=list(map(int,input().split()))
        d+=c[1]-c[0]
    print(a-d if a>d else 'OK')