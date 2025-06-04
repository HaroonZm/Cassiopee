while True:
    T, D, L = map(int, input().split())
    if T == 0:
        exit()
    XXX = [int(input()) for _ in range(T)]
    limit_time = 0
    ans = 0
    swet_time = 0
    for i, x in enumerate(XXX):
        if limit_time > 0:
            swet_time += 1
            limit_time -= 1
        if x >= L:
            limit_time = D
        if limit_time == 0:
            ans += swet_time
            swet_time = 0
        elif i == len(XXX) - 1:
            ans += swet_time
    print(ans)