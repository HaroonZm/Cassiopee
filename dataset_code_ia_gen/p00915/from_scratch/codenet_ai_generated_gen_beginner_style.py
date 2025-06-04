while True:
    n, l = map(int, input().split())
    if n == 0 and l == 0:
        break
    ants = []
    for i in range(n):
        d, p = input().split()
        p = int(p)
        ants.append({'num': i+1, 'dir': d, 'pos': p})
    last_time = -1
    last_ant = -1
    last_side = ''  # 'L' or 'R' - side through which last ant exits
    for ant in ants:
        if ant['dir'] == 'L':
            time_to_exit = ant['pos']
            side = 'L'
        else:
            time_to_exit = l - ant['pos']
            side = 'R'
        if time_to_exit > last_time:
            last_time = time_to_exit
            last_ant = ant['num']
            last_side = side
        elif time_to_exit == last_time:
            # if tied time, prefer ant leaving left side
            if side == 'L' and last_side == 'R':
                last_ant = ant['num']
                last_side = side
    print(last_time, last_ant)