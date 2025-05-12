def inpl(): return list(map(int, input().split()))
MOD = 10**9 + 7

a, b, x = inpl()
if x < a:
    print(x%MOD)
else:
    e = (x-b)//(a-b)
    print((x + e*b)%MOD)