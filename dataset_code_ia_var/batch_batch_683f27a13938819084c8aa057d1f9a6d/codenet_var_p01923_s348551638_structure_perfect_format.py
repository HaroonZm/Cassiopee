while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    l = [0] * M
    for i in range(N):
        d, v = map(int, input().split())
        if l[d - 1] < v:
            l[d - 1] = v
    total = 0
    for i in range(M):
        total += l[i]
    print(total)