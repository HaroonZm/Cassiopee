while True:
    TPR = raw_input().split()
    T = int(TPR[0])
    P = int(TPR[1])
    R = int(TPR[2])
    if T == 0 and P == 0 and R == 0:
        break

    wrong = []
    pen = []
    for i in range(T):
        wrong.append([0] * P)
        pen.append([0] * P)

    for i in range(R):
        parts = raw_input().split()
        t = int(parts[0]) - 1
        p = int(parts[1]) - 1
        time = int(parts[2])
        mes = parts[3]
        if pen[t][p] == 0:
            if mes == "CORRECT":
                pen[t][p] = wrong[t][p] * 1200 + time
            else:
                wrong[t][p] += 1

    result = []
    for i in range(T):
        solved = 0
        total_penalty = 0
        for j in range(P):
            if pen[i][j] != 0:
                solved += 1
                total_penalty += pen[i][j]
        result.append(( -solved, total_penalty, i + 1))
    result.sort()
    for r in result:
        print r[2], -r[0], r[1]