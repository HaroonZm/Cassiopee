def bowling_score(rolls):
    score = 0
    roll_index = 0
    for frame in range(10):
        if frame < 9:
            if rolls[roll_index] == 10:  # strike
                score += 10 + rolls[roll_index + 1] + rolls[roll_index + 2]
                roll_index += 1
            elif rolls[roll_index] + rolls[roll_index + 1] == 10:  # spare
                score += 10 + rolls[roll_index + 2]
                roll_index += 2
            else:
                score += rolls[roll_index] + rolls[roll_index + 1]
                roll_index += 2
        else:  # 10th frame
            score += sum(rolls[roll_index:roll_index + 3])
            break
    return score

import sys
input = sys.stdin.readline
while True:
    m = input()
    if not m:
        break
    m = m.strip()
    if m == '0':
        break
    m = int(m)
    results = []
    for _ in range(m):
        data = list(map(int, input().split()))
        id_, rolls = data[0], data[1:]
        s = bowling_score(rolls)
        results.append((id_, s))
    results.sort(key=lambda x: (-x[1], x[0]))
    for r in results:
        print(r[0], r[1])