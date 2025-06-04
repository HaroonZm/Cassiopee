while True:
    n = int(input())
    if n == 0:
        break
    _in = input().split(' ')
    f_stat = [False, False]
    state = False
    cnt = 0
    for i in range(n):
        com = _in[i]
        if com == "lu":
            f_stat[0] = True
        elif com == "ru":
            f_stat[1] = True
        elif com == "ld":
            f_stat[0] = False
        else:
            f_stat[1] = False
        if not state:
            if f_stat[0] and f_stat[1]:
                cnt += 1
                state = True
        else:
            if not f_stat[0] and not f_stat[1]:
                cnt += 1
                state = False
    print(cnt)