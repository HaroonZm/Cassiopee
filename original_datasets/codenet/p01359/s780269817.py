import bisect
while True:
    N,Q = map(int,input().split())
    if N == 0: break
    src = []
    for i in range(N):
        n,l,y = input().split()
        src.append((int(y), int(l), n))
    src.sort()
    for i in range(Q):
        q = int(input())
        a = bisect.bisect(src,(q,-1,-1))
        if a < N:
            y,l,n = src[a]
            if y-l < q <= y:
                print(n + ' ' + str(q-y+l))
                continue
        if a+1 < N:
            y,l,n = src[a+1]
            if y-l < q <= y:
                print(n + ' ' + str(q-y+l))
                continue
        print('Unknown')