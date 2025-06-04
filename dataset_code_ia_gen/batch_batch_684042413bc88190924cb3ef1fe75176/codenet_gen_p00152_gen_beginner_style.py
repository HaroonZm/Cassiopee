def calculate_score(rolls):
    score = 0
    frame = 1
    i = 0
    while frame <= 10:
        if frame < 10:
            # strike
            if rolls[i] == 10:
                score += 10 + rolls[i+1] + rolls[i+2]
                i += 1
            # spare
            elif rolls[i] + rolls[i+1] == 10:
                score += 10 + rolls[i+2]
                i += 2
            else:
                score += rolls[i] + rolls[i+1]
                i += 2
            frame += 1
        else:
            # 10th frame
            # sum all remaining rolls in 10th frame (2 or 3 rolls)
            score += sum(rolls[i:])
            frame += 1
    return score

while True:
    m = input()
    if m == '0':
        break
    m = int(m)
    players = []
    for _ in range(m):
        data = input().split()
        id_num = int(data[0])
        rolls = list(map(int, data[1:]))
        total_score = calculate_score(rolls)
        players.append((id_num, total_score))
    # sort by score desc, id asc
    players.sort(key=lambda x: (-x[1], x[0]))
    for p in players:
        print(p[0], p[1])