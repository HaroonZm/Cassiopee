def main():
    while 1:
        N, M = map(int, input().split())
        if N == M == 0:
            break
        data = [0]*(M+1)
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
        M0 = 2**(M-1).bit_length()
        def lower_bound(x):
            w = i = 0
            k = M0
            while k:
                if i+k <= M and w + data[i+k] <= x:
                    w += data[i+k]
                    i += k
                k >>= 1
            return i+1
        *K, = map(int, input().split())
        su = 0
        ans = 0
        for k in K:
            su = (su + k) % M
            v = get(su+1)
            w = lower_bound(v)-1
            if w == M:
                w = 0
            ans = max(ans, (su - w) % M)
            add(su+1, 1)
        print(ans)
main()