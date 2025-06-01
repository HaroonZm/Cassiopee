while 1:
    m = int(raw_input())
    if m == 0:
        break

    card = []
    total = 0
    for i in range(m):
        a, b = map(int, raw_input().split())
        card.append([a, b])
        total += a * b
    card = sorted(card, reverse=True)

    B = [0] * (total + 1)
    for a, b in card:
        A = B[:]
        B = [0] * (total + 1)
        B[a:a * b + 1:a] = [1] * b
        for i in range(total, -1, -1):
            if A[i]:
                for e in range(i, i + a * b + 1, a):
                    B[e] += A[i]

    g = int(raw_input())
    for _ in range(g):
        n = int(raw_input())
        if 0 <= n <= total:
            print B[n]
        else:
            print 0