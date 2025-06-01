def score_game(rolls):
    score = 0
    roll_index = 0
    for frame in range(10):
        if frame < 9:
            if rolls[roll_index] == 10:  # strike
                score += 10 + rolls[roll_index+1] + rolls[roll_index+2]
                roll_index += 1
            elif rolls[roll_index] + rolls[roll_index+1] == 10:  # spare
                score += 10 + rolls[roll_index+2]
                roll_index += 2
            else:
                score += rolls[roll_index] + rolls[roll_index+1]
                roll_index += 2
        else:
            score += sum(rolls[roll_index:roll_index+3]) if sum(rolls[roll_index:roll_index+2]) >= 10 else sum(rolls[roll_index:roll_index+2])
    return score

import sys
lines = sys.stdin.read().strip().split('\n')
idx = 0
while True:
    if idx>=len(lines):
        break
    m = lines[idx]
    idx += 1
    if m == '0': break
    m = int(m)
    players = []
    for _ in range(m):
        data = list(map(int, lines[idx].split()))
        idx += 1
        pid = data[0]
        rolls = data[1:]
        players.append((pid, score_game(rolls)))
    players.sort(key=lambda x: (-x[1], x[0]))
    for p in players:
        print(p[0], p[1])