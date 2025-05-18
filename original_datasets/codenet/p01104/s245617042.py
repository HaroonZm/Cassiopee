while 1:
    n, m = map(int, input().split())
    if n+m == 0:
        break
    B = [int(input(),2) for i in range(n)]
    C = {0: 0}
    for b in B:
        *D, = C.items()
        for k, v in D:
            C[k^b] = max(C.get(k^b, 0), v+1)
    print(C[0])