from decimal import Decimal, getcontext
d1 = Decimal(1)
while True:
    n,k,m,r = map(int,input().split())
    if n == 0:
        break
    getcontext().prec = r + 1
    ans = d1 / Decimal(n)
    if m != 0:
        s = 0
        for i in range(1,n):
            s += d1 / Decimal(i)
        ans = ans * (1 + s)
    fmt = '{:.' + str(r + 1) + 'f}'
    out = fmt.format(ans)
    print(out[:-1])