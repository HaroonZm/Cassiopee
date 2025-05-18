while True:
    n, m, a = list(map(int, input().split()))
    if n == 0:
        break
    hpq = []
    for i in range(m):
        h, p, q = list(map(int, input().split()))
        hpq.append([h, p, q])
    hpq = sorted(hpq, key=lambda x: x[0], reverse=True)
    for i in reversed(range(1, hpq[0][0] + 1)):
        for j in range(m):
            if hpq[j][0] > i:
                continue
            elif hpq[j][0] < i:
                break
            elif hpq[j][0] == i and hpq[j][1] != a and hpq[j][2] != a:
                continue
            elif hpq[j][0] == i and hpq[j][1] != a and hpq[j][2] == a:
                a = hpq[j][1]
                break
            elif hpq[j][0] == i and hpq[j][1] == a and hpq[j][2] != a:
                a = hpq[j][2]
                break
    print(a)