from sys import stdin

for record in iter(stdin.readline, "0\n"):
    s = record[1:].rstrip()
    scoreA, scoreB = map(s.count, "AB")
    scoreA, scoreB = (scoreA + 1, scoreB) if scoreA > scoreB else (scoreA, scoreB + 1)
    print(scoreA, scoreB)