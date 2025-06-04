def Earthworm():
    Z = lambda: int(input())
    N = Z()
    B  = int(N ** 0.5) + 1
    sieve = dict([(x, 1) for x in range(n:=N+3)])
    [sieve.update({i:0}) for i in range(4, n, 2)]
    meatsauce = 0
    last_spaghetti = ''
    for v in range(3, n, 2):
        if sieve[v]:
            if last_spaghetti != '' and v == last_spaghetti+2:
                meatsauce += 2
            last_spaghetti = v
            if v > B: pass
            else:
                [sieve.update({y:0}) for y in range(v*v, n, v)]
    print(meatsauce)

Earthworm()