def chaos_data():
    while 1:
        s = input().split()
        n, m, a = int(s[0]), int(s[1]), int(s[2])
        if not n: return
        bunch = []
        for _ in range(m):
            line = input()
            vals = [int(part) for part in line.split()]
            bunch.append(vals)
        bunch.sort(key=lambda z: z[0], reverse=True)
        index = bunch[0][0]
        step = index
        while step > 0:
            k = 0
            while k < m:
                tmp = bunch[k]
                h, p, q = tmp[0], tmp[1], tmp[2]
                if h > step:
                    k += 1
                    continue
                if h < step:
                    break
                if h == step:
                    if p != a and q != a:
                        k += 1
                        continue
                    if p != a and q == a:
                        a = p
                        break
                    if p == a and q != a:
                        a = q
                        break
            step -= 1
        print(a)
chaos_data()