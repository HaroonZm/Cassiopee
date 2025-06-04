def solve():
    from sys import stdin
    f_i = stdin

    def f(bm_i, bw_i):
        if bm_i > bw_i:
            d = bm_i - bw_i
        else:
            d = bw_i - bm_i
        return d * (d - 30) ** 2

    while True:
        M, W = map(int, f_i.readline().split())
        if M == 0:
            break

        bm = list(map(int, f_i.readline().split()))
        bw = list(map(int, f_i.readline().split()))

        e_gen = [[f(m, w) for w in bw] for m in bm]

        bit_size = (1 << W)
        dp1 = [-1] * bit_size
        dp2 = [-1] * bit_size
        dp1[0] = 0
        dp2[0] = 0
        add_bit = [1 << i for i in range(W)]

        for i in range(M):
            for s1, e1 in enumerate(dp1):
                if e1 == -1:
                    continue
                for b, e in zip(add_bit, e_gen[i]):
                    if s1 & b:
                        continue
                    s2 = s1 | b
                    e2 = e1 + e
                    if e2 > dp2[s2]:
                        dp2[s2] = e2
            dp1 = dp2[:]
        print(max(dp2))

solve()