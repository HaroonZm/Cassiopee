H, W, A, B = map(int, input().split())
h = {}
p = 10**9+7
q = p - 2
for x in range(H+W-1):
    if h.get(x-1):
        a = (x * h[x-1][0]) % p
    else:
        a = 1
    b = pow(a,q,p)
    h[x] = (a,b)

def C(n, r):
    return h[n][0] * h[r][1] * h[n-r][1]

ans = 0
for i in range(B, W):
    ans += C(i+H - A - 1, i) * C(W - 1 - i + A - 1, W - 1 - i)

print(ans % p)