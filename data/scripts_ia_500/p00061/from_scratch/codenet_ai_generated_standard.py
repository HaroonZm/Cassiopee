teams = {}
while True:
    line = input()
    if line == "":
        break
    p, s = line.split(',')
    p, s = int(p), int(s)
    if p == 0 and s == 0:
        break
    teams[p] = s
scores = sorted(set(teams.values()), reverse=True)
rank = {score: i+1 for i, score in enumerate(scores)}
try:
    while True:
        q = input()
        if q == "":
            break
        q = int(q)
        print(rank[teams[q]])
except EOFError:
    pass