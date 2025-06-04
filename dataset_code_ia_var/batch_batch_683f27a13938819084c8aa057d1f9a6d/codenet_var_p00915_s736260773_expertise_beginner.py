while True:
    n_l = raw_input().split()
    n = int(n_l[0])
    l = int(n_l[1])
    if n == 0:
        break

    R = []
    L = []
    for i in range(l-1):
        R.append(0)
        L.append(0)

    for i in range(1, n+1):
        d_p = raw_input().split()
        d = d_p[0]
        p = int(d_p[1]) - 1
        if d == "R":
            R[p] = i
        else:
            L[p] = i

    t = 0
    num = 0
    while sum(R) + sum(L) != 0:
        if R[l-2] > 0:
            num = R[l-2]
        tempR = [0]
        for j in range(l-2):
            tempR.append(R[j])
        R = tempR

        if L[0] > 0:
            num = L[0]
        tempL = []
        for j in range(1, l-1):
            tempL.append(L[j])
        tempL.append(0)
        L = tempL

        for i in range(l-1):
            if L[i] > 0 and R[i] > 0:
                a = L[i]
                L[i] = R[i]
                R[i] = a
        t += 1

    print t, num