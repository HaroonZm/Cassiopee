def main():
    while True:
        N_M = input().split()
        N = int(N_M[0])
        M = int(N_M[1])
        if N == 0 and M == 0:
            break

        data = [0] * (M + 1)

        def add(k, x):
            while k <= M:
                data[k] += x
                k += k & -k

        def get(k):
            s = 0
            while k:
                s += data[k]
                k -= k & -k
            return s

        M0 = 1
        while M0 < M:
            M0 *= 2

        def lower_bound(x):
            w = 0
            i = 0
            k = M0
            while k:
                if i + k <= M and w + data[i + k] <= x:
                    w += data[i + k]
                    i += k
                k //= 2
            return i + 1

        K = list(map(int, input().split()))
        su = 0
        ans = 0
        for k in K:
            su = (su + k) % M
            v = get(su + 1)
            w = lower_bound(v) - 1
            if w == M:
                w = 0
            ans = max(ans, (su - w) % M)
            add(su + 1, 1)
        print(ans)

main()