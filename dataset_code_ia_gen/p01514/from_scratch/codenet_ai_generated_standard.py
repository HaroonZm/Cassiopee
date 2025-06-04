while True:
    T, P, R = map(int, input().split())
    if T == 0 and P == 0 and R == 0:
        break
    solved = [0]*(T+1)
    penalty = [0]*(T+1)
    wrong = [[0]*(P+1) for _ in range(T+1)]
    solved_flag = [[False]*(P+1) for _ in range(T+1)]
    for _ in range(R):
        tID, pID, time, msg = input().split()
        tID = int(tID)
        pID = int(pID)
        time = int(time)
        if solved_flag[tID][pID]:
            continue
        if msg == 'CORRECT':
            solved[tID] += 1
            penalty[tID] += wrong[tID][pID]*1200 + time
            solved_flag[tID][pID] = True
        else:  # WRONG
            wrong[tID][pID] += 1
    rank = list(range(1,T+1))
    rank.sort(key=lambda x:(-solved[x], penalty[x], x))
    for r in rank:
        print(r, solved[r], penalty[r])