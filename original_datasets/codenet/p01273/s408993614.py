while True:
    N, M = map(int, raw_input().split())
    if N == 0:
        break
    ls = []
    for i in range(M):
        t, s, d = map(int, raw_input().split())
        ls.append((t, s, d))
    ls.sort()
    cnt = [0, 1] + [0] * N
    for p in ls:
        cnt[p[2]] = max(cnt[p[1]], cnt[p[2]])
    print sum(cnt)