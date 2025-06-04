while True:
    vals = raw_input().split()
    N = int(vals[0])
    M = int(vals[1])
    if N == 0:
        break
    ls = []
    for i in range(M):
        t, s, d = raw_input().split()
        t = int(t)
        s = int(s)
        d = int(d)
        ls.append((t, s, d))
    ls.sort()
    cnt = [0] * (N + 2)
    cnt[1] = 1
    for p in ls:
        t = p[0]
        s = p[1]
        d = p[2]
        if cnt[d] < cnt[s]:
            cnt[d] = cnt[s]
    total = 0
    for x in cnt:
        total += x
    print total