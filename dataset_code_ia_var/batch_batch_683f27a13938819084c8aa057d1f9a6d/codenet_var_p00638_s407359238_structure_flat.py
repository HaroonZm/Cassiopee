while True:
    n = int(input())
    if n == 0:
        break
    bridges = []
    i = 0
    while i < n:
        s = input().split()
        t = int(s[0])
        b = int(s[1])
        bridges.append((t, b))
        i += 1

    # Tri brut (pas de lambda, structure plate)
    for i in range(len(bridges)):
        for j in range(i + 1, len(bridges)):
            if bridges[i][1] > bridges[j][1]:
                tmp = bridges[i]
                bridges[i] = bridges[j]
                bridges[j] = tmp

    flag = True
    sumt = 0
    i = 0
    while i < len(bridges):
        sumt += bridges[i][0]
        if sumt > bridges[i][1]:
            flag = False
            break
        i += 1

    if flag:
        print('Yes')
    else:
        print('No')