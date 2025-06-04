from math import gcd

for _ in range(int(input())):
    A, M = map(int, input().split())
    a = A
    m = M
    n = 1
    stack = []
    while True:
        if gcd(a, m) == 1:
            if m == 1:
                res = 1
                break
            phi = m
            temp_n = m
            x = 2
            while x <= int(temp_n ** 0.5) + 1:
                if temp_n % x == 0:
                    phi = (phi // x) * (x - 1)
                    while temp_n % x == 0:
                        temp_n //= x
                x += 1
            if temp_n != 1:
                phi = (phi // temp_n) * (temp_n - 1)
            G = gcd(phi, m)
            stack.append((a, m, n, phi, G))
            # Recurse "simulate"
            a = a
            m = G
            n = n
            continue
        else:
            # biggcd section (simulate recursion)
            g = gcd(a, m)
            resg = g
            countg = 2
            while gcd(g ** countg, m) > resg:
                resg = gcd(g ** countg, m)
                countg += 1
            big = resg
            # Recurse "simulate"
            a = a
            m = m // big
            n = n * big
            stack.append(('big', big))
            continue

    # Now process "return stack"
    while stack:
        ctx = stack.pop()
        if isinstance(ctx, tuple) and ctx[0] == 'big':
            big = ctx[1]
            res = big * res
        else:
            a, m, n, phi, G = ctx
            mod = m * phi // G
            r0 = res
            temp = pow(a, n * r0, mod) - n * r0
            temp = ((temp % mod) // G)
            temp2 = pow(n * phi // G, phi - 1, m)
            res = (temp * temp2 * phi + r0) % mod
    print(res)