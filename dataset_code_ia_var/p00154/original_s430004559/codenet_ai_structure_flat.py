while 1:
    m = int(raw_input())
    if m == 0: break

    card = []
    total = 0
    for i in range(m):
        a, b = map(int, raw_input().split())
        card.append((a, b))
        total += a * b
    card.sort(reverse=True)

    B = [0] * (total + 1)
    B[0] = 1
    for a, b in card:
        for t in range(total, -1, -1):
            if B[t]:
                for k in range(1, b + 1):
                    if t + a * k <= total:
                        B[t + a * k] += B[t]
                    else:
                        break

    g = int(raw_input())
    for _ in range(g):
        n = int(raw_input())
        if 0 <= n <= total:
            print B[n]
        else:
            print 0