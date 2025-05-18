while True:
    N=int(input())
    if N== 0:
        break
    B=0
    V=0
    for i in range(N):
        p,d,g=map(int,input().split())
        S=d+g
        if S>V:
            V=S
            B=p
    print(B,V)