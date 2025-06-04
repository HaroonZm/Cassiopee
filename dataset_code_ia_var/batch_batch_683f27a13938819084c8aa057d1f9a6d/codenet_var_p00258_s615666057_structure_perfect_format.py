bc = [bin(i).count('1') for i in range(65536)]

def solve():
    from sys import stdin
    f_i = stdin

    while True:
        n, c = map(int, f_i.readline().split())
        if n == 0:
            break

        A = [int(f_i.readline().replace(' ', ''), 2) for _ in range(n)]
        B = [int(f_i.readline().replace(' ', ''), 2) for _ in range(c)]

        dp1 = {A[0]: 0}
        dp2 = {}

        for a in A[1:] + [0]:
            for st1, sc1 in dp1.items():
                for b in B:
                    cb = st1 & b
                    sc2 = sc1 + bc[cb]
                    st2 = (st1 - cb) | a
                    if st2 in dp2:
                        if dp2[st2] < sc2:
                            dp2[st2] = sc2
                    else:
                        dp2[st2] = sc2
            dp1, dp2 = dp2, {}

        print(max(dp1.values()))

solve()