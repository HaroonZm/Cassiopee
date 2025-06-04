def last_ant():
    while True:
        n, l = map(int, input().split())
        if n == 0 and l == 0:
            break
        ants = []
        for i in range(1, n+1):
            d, p = input().split()
            p = int(p)
            dir_ = -1 if d == 'L' else 1
            ants.append((i, p, dir_))
        times = []
        for i, p, dir_ in ants:
            if dir_ == -1:
                times.append((p, i, 'L'))
            else:
                times.append((l - p, i, 'R'))
        max_t = max(t[0] for t in times)
        last_ants = [t for t in times if t[0] == max_t]
        left_exit_ants = [a for a in last_ants if a[2] == 'L']
        if left_exit_ants:
            res = min(left_exit_ants, key=lambda x: x[1])
        else:
            res = min(last_ants, key=lambda x: x[1])
        print(max_t, res[1])
last_ant()