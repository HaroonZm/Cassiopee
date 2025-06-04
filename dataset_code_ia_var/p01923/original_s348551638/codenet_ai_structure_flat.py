while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    l = []
    for _ in range(M):
        l.append(0)
    i = 0
    while i < N:
        d, v = map(int, input().split())
        if l[d - 1] < v:
            l[d - 1] = v
        i += 1
    total = 0
    j = 0
    while j < M:
        total += l[j]
        j += 1
    print(total)