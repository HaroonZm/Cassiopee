n, l = map(int, raw_input().split())
while n != 0:
    tube = []
    for i in range(l - 1):
        tube.append([])
    for i in range(1, n + 1):
        d, p = raw_input().split()
        p = int(p)
        if d == "R":
            tube[p - 1].append(i)
        else:
            tube[p - 1].append(-i)
    t = 0
    num = 0
    done = False
    while not done:
        # Check if all tubes are empty
        is_empty = True
        for lst in tube:
            if len(lst) > 0:
                is_empty = False
                break
        if is_empty:
            done = True
            break
        for s in [-1, 1]:
            if s == -1:
                rng = range(l - 2, -1, -1)
            else:
                rng = range(0, l - 1)
            for i in rng:
                new_lst = []
                for a in tube[i]:
                    if -s * a > 0:
                        # Remove from current tube and move
                        if (s == -1 and i == l - 2) or (s == 1 and i == 0):
                            num = abs(a)
                        else:
                            tube[i - s].append(a)
                    else:
                        new_lst.append(a)
                tube[i] = new_lst
        for i in range(l - 1):
            if len(tube[i]) > 1:
                tube[i] = [-a for a in tube[i]]
        t += 1
    print t, num
    n, l = map(int, raw_input().split())