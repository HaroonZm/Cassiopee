try:
    while True:
        n_m = raw_input()
        n, m = [int(_) for _ in n_m.split()]
        if n == 0 and m == 0:
            break

        h = []
        count = 0
        while count < n:
            line = raw_input()
            h.append(int(line))
            count += 1

        w = []
        count = 0
        while count < m:
            line = raw_input()
            w.append(int(line))
            count += 1

        hs = {}
        i = 0
        while i < n:
            h0 = 0
            j = i
            while j < n:
                h0 += h[j]
                if h0 in hs:
                    hs[h0] += 1
                else:
                    hs[h0] = 1
                j += 1
            i += 1

        ans = 0
        i = 0
        while i < m:
            w0 = 0
            j = i
            while j < m:
                w0 += w[j]
                ans += hs.get(w0, 0)
                j += 1
            i += 1

        print(ans)
except EOFError:
    pass