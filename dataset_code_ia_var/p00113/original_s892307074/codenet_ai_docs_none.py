while True:
    try:
        p, q = list(map(int, input().split()))
    except:
        break
    rr = [-1]*q
    rr[p] = 0
    ans = ''
    for k in range(1, q):
        p *= 10
        ans += str(p // q)
        r = p % q
        if r == 0 or rr[r] >= 0:
            print(ans)
            if rr[r] >= 0:
                print(*[' ']*rr[r], *['^']*(k-rr[r]), sep='')
            break
        rr[r], p = k, r