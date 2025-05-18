while True:
    T, P, R = map(int, input().split())
    if T == 0 and P == 0 and R == 0:
        break
    correct = [[0] * (P+1) for _ in range(T+1)]
    wrong = [[0] * (P+1) for _ in range(T+1)]
    penalty = [0] * (T+1)
    for i in range(R):
        data = input().split()
        team = int(data[0])
        prob = int(data[1])
        time = int(data[2])
        if data[3] == 'WRONG':
            wrong[team][prob] += 1
        else:
            if correct[team][prob] == 0:
                correct[team][prob] = 1
                penalty[team] += wrong[team][prob]*1200 + time
    res = []
    for i in range(1,T+1):
        res.append((i, sum(correct[i]), penalty[i]))
        res.sort(key=lambda x:(x[1],-1*x[2],-1*x[0]), reverse=True)
    for i in range(T):
        print(res[i][0],res[i][1],res[i][2])