from functools import reduce
while True:
    n = input()
    if n == '0000':
        break
    if len(n) < 4:
        n = n.zfill(4)
    all_same = True
    for s in n:
        if n[0] != s:
            all_same = False
            break
    if all_same:
        print('NA')
    else:
        cnt = 0
        while n != '6174':
            l_list = sorted(n, reverse=True)
            l = ''.join(l_list)
            s_list = sorted(n)
            s = ''.join(s_list)
            n = str(int(l) - int(s))
            if len(n) < 4:
                n = n.zfill(4)
            cnt += 1
        print(cnt)