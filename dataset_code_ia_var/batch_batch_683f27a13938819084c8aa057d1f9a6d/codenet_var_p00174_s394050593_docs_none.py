while True:
    record = input()
    if record == "0":
        break
    scoreA = record[1:].count("A")
    scoreB = record[1:].count("B")
    if scoreA > scoreB:
        scoreA += 1
    else:
        scoreB += 1
    print(scoreA, scoreB)