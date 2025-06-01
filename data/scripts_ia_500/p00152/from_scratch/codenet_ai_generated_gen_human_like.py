def calc_score(rolls):
    score = 0
    frame = 0
    i = 0
    while frame < 10:
        if rolls[i] == 10:  # strike
            score += 10 + rolls[i + 1] + rolls[i + 2]
            i += 1
        elif rolls[i] + rolls[i + 1] == 10:  # spare
            score += 10 + rolls[i + 2]
            i += 2
        else:
            score += rolls[i] + rolls[i + 1]
            i += 2
        frame += 1
    return score

def main():
    import sys
    for line in sys.stdin:
        line=line.strip()
        if line == '0':
            break
        m = int(line)
        players = []
        for _ in range(m):
            data = sys.stdin.readline().strip().split()
            id = int(data[0])
            rolls = list(map(int, data[1:]))

            # For the 10th frame, the number of rolls can vary

            # Because rolls length is between 12 and 21, and bowling rules apply,
            # simply calculate score as per bowling scoring rules.

            players.append((id, calc_score(rolls)))
        # sort by score descending, then by id ascending
        players.sort(key=lambda x: (-x[1], x[0]))
        for p in players:
            print(p[0], p[1])

if __name__ == '__main__':
    main()