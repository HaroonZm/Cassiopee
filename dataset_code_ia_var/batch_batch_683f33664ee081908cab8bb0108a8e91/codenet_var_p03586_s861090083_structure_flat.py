Q = int(input())
for _ in range(Q):
    A, M = map(int, input().split())
    if M == 1:
        print(1)
    else:
        a = A
        mod = M

        # Factorization and Torshent (Euler's totient)
        n = mod
        base_n = n
        dic = {}
        p = 2
        curr_n = n
        while curr_n != 1:
            i = 0
            while curr_n % p == 0:
                i += 1
                curr_n //= p
            if i != 0:
                dic[p] = i
            p += 1
            if p * p > base_n and curr_n != 1:
                dic[curr_n] = 1
                break
        S = n
        for i in dic:
            S //= i
            S *= i - 1
        M_ = S

        # GCD
        x = M_
        y = mod
        while y != 0:
            x, y = y, x % y
        MM = x

        # Compute Resque(a, MM) recursively, unrolled manually
        # Since this is a flat structure, simulate the stack manually
        # We'll use a stack of (a, mod, state, variables...)

        stack = [(a, MM, 0, None, None, None, None, None, None, None)]
        res_stack = []
        final_result = None
        while stack:
            current = stack[-1]
            a2, mod2, state, k, m, modmod, Tm, invm, t, R = current
            if mod2 == 1:
                res_stack.append(1)
                stack.pop()
                continue
            if state == 0:
                # Factorization and Torshent for inner mod2
                n2 = mod2
                base_n2 = n2
                dic2 = {}
                p2 = 2
                curr_n2 = n2
                while curr_n2 != 1:
                    i2 = 0
                    while curr_n2 % p2 == 0:
                        i2 += 1
                        curr_n2 //= p2
                    if i2 != 0:
                        dic2[p2] = i2
                    p2 += 1
                    if p2 * p2 > base_n2 and curr_n2 != 1:
                        dic2[curr_n2] = 1
                        break
                S2 = n2
                for ii in dic2:
                    S2 //= ii
                    S2 *= ii - 1
                M2 = S2

                # GCD
                x2 = M2
                y2 = mod2
                while y2 != 0:
                    x2, y2 = y2, x2 % y2
                MM2 = x2

                stack[-1] = (a2, mod2, 1, None, None, None, None, None, None, None)
                stack.append((a2, MM2, 0, None, None, None, None, None, None, None))
                continue
            elif state == 1:
                R2 = res_stack.pop()
                # doubling(a, R2, mod2)
                y3 = 1
                base3 = a2
                m3 = R2
                while m3 != 0:
                    if m3 % 2 == 1:
                        y3 *= base3
                        y3 %= mod2
                    base3 *= base3
                    base3 %= mod2
                    m3 //= 2
                k = y3

                # m, modmod
                # we need the M2, MM2 we found above
                # Recompute for flatness
                n2 = mod2
                base_n2 = n2
                dic2 = {}
                p2 = 2
                curr_n2 = n2
                while curr_n2 != 1:
                    i2 = 0
                    while curr_n2 % p2 == 0:
                        i2 += 1
                        curr_n2 //= p2
                    if i2 != 0:
                        dic2[p2] = i2
                    p2 += 1
                    if p2 * p2 > base_n2 and curr_n2 != 1:
                        dic2[curr_n2] = 1
                        break
                S2 = n2
                for ii in dic2:
                    S2 //= ii
                    S2 *= ii - 1
                M2 = S2
                x2 = M2
                y2 = mod2
                while y2 != 0:
                    x2, y2 = y2, x2 % y2
                MM2 = x2

                m = M2 // MM2
                modmod = mod2 // MM2

                # Torshent for modmod
                n3 = modmod
                base_n3 = n3
                dic3 = {}
                p3 = 2
                curr_n3 = n3
                while curr_n3 != 1:
                    i3 = 0
                    while curr_n3 % p3 == 0:
                        i3 += 1
                        curr_n3 //= p3
                    if i3 != 0:
                        dic3[p3] = i3
                    p3 += 1
                    if p3 * p3 > base_n3 and curr_n3 != 1:
                        dic3[curr_n3] = 1
                        break
                S3 = n3
                for iii in dic3:
                    S3 //= iii
                    S3 *= iii - 1
                Tm = S3

                # inverse of m modulo modmod by doubling(m, Tm-1, modmod)
                y4 = 1
                base4 = m
                m4 = Tm - 1
                while m4 != 0:
                    if m4 % 2 == 1:
                        y4 *= base4
                        y4 %= modmod
                    base4 *= base4
                    base4 %= modmod
                    m4 //= 2
                invm = y4

                t = ((k - R2) // MM2) * invm
                R = R2 + t * M2
                R %= (mod2 * M2 // MM2)
                R += (mod2 * M2 // MM2)
                res_stack.append(R)
                stack.pop()
                continue

        R = res_stack.pop()
        print(R)