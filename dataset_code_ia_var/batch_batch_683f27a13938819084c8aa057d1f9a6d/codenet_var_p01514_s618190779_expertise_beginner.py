t, p, r = map(int, raw_input().split())
while t != 0:
    penalty = [0] * t
    solved = [[False for j in range(p)] for i in range(t)]
    mistakes = [[0 for j in range(p)] for i in range(t)]
    solved_count = [0] * t
    for i in range(r):
        parts = raw_input().split()
        tid = int(parts[0]) - 1
        pid = int(parts[1]) - 1
        time = int(parts[2])
        message = parts[3]
        if solved[tid][pid]:
            continue
        if message == "CORRECT":
            solved[tid][pid] = True
            penalty[tid] += mistakes[tid][pid] * 1200 + time
            solved_count[tid] += 1
        else:
            mistakes[tid][pid] += 1
    ranking = []
    for i in range(t):
        ranking.append([-solved_count[i], penalty[i], i])
    ranking.sort()
    for line in ranking:
        print line[2] + 1, -line[0], line[1]
    t, p, r = map(int, raw_input().split())