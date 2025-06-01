n,m = (lambda x: list(map(int, x.split())))(input())
a = list(map(int, (lambda f: [f() for _ in range(n)])(lambda: input())))

k = 0
while k < m:
    i = 0
    while i < n-1:
        mod_base = k+1
        left, right = a[i] % mod_base, a[i+1] % mod_base
        if left > right:
            a[i], a[i+1] = a[i+1], a[i]
        i += 1
    k += 1

print('\n'.join(str(x) for x in a))