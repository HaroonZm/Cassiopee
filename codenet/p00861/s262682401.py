while True:
    lst = []
    S = raw_input()
    if S == '.':
        break
    lst.append(S)
    while True:
        S = raw_input()
        if S == '.':
            break
        lst.append(S)
    
    upper = []
    flag = False

    for i in range(len(lst)):
        S = lst[i]
        if '=' in S:
            try:
                exec(S)
            except:
                flag = True
            for elem in upper:
                for key in elem[0]:
                    if key >= elem[1]:
                        flag = True
                        break
            if flag:
                print i + 1
                break
        else:
            P = S.split('[')
            name = P[0]
            num = int(P[1][:-1])
            exec(name + ' = {}')
            upper.append((globals()[name], num))
    
    if not flag:
        print 0