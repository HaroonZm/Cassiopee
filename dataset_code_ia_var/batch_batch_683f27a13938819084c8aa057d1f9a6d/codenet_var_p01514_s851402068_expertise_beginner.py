while True:
    line = input()
    T, P, R = map(int, line.split())
    if T == 0 and P == 0 and R == 0:
        break

    correct = []
    wrong = []
    for i in range(T+1):
        correct.append([0] * (P+1))
        wrong.append([0] * (P+1))

    penalty = [0] * (T+1)

    for i in range(R):
        parts = input().split()
        team = int(parts[0])
        prob = int(parts[1])
        time = int(parts[2])
        res_type = parts[3]
        if res_type == "WRONG":
            wrong[team][prob] += 1
        else:
            if correct[team][prob] == 0:
                correct[team][prob] = 1
                penalty[team] = penalty[team] + wrong[team][prob]*1200 + time

    res = []
    for i in range(1, T+1):
        num_correct = sum(correct[i])
        res.append([i, num_correct, penalty[i]])

    # Tri du classement
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            # On veut trier par nb correct en décroissant, puis penalty en croissant, puis team en croissant
            if res[j][1] > res[i][1] or (res[j][1] == res[i][1] and res[j][2] < res[i][2]) or (res[j][1] == res[i][1] and res[j][2] == res[i][2] and res[j][0] < res[i][0]):
                temp = res[i]
                res[i] = res[j]
                res[j] = temp

    for i in range(T):
        print(res[i][0], res[i][1], res[i][2])