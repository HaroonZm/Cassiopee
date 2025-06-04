while True:
    w, d = input().split()
    w = int(w)
    d = int(d)
    if w == 0 and d == 0:
        break

    h = input().split()
    for i in range(len(h)):
        h[i] = int(h[i])

    m = input().split()
    for i in range(len(m)):
        m[i] = int(m[i])

    hl = []
    ml = []
    for i in range(30):
        hl.append(0)
        ml.append(0)

    for i in h:
        hl[i] = hl[i] + 1
    for i in m:
        ml[i] = ml[i] + 1

    ans = 0
    for i in range(30):
        if hl[i] > ml[i]:
            ans = ans + i * hl[i]
        else:
            ans = ans + i * ml[i]

    print(ans)