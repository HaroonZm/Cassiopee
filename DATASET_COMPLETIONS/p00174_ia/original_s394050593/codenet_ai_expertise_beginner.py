while True:
    record = input()
    if record == "0":
        break
    part = record[1:]
    scoreA = 0
    scoreB = 0
    for c in part:
        if c == "A":
            scoreA = scoreA + 1
        elif c == "B":
            scoreB = scoreB + 1
    if scoreA > scoreB:
        scoreA = scoreA + 1
    else:
        scoreB = scoreB + 1
    print(scoreA, scoreB)