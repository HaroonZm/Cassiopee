while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    maxv=[0]*(M+1)
    for _ in range(N):
        d,v=map(int,input().split())
        if v>maxv[d]:
            maxv[d]=v
    print(sum(maxv[1:]))