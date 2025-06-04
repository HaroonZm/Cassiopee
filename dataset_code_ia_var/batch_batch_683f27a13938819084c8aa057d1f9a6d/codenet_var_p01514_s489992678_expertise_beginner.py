continue_program = True

while continue_program:
    tpr = input().split()
    t = int(tpr[0])
    p = int(tpr[1])
    r = int(tpr[2])

    if t == 0:
        continue_program = False
        continue

    data = []
    for i in range(t):
        data.append([i + 1, 0, 0]) # [Team ID, Problems Solved, Total Penalty]

    wrong = []
    for i in range(t):
        wrong.append([0] * p)

    for _ in range(r):
        log = input().split()
        team = int(log[0]) - 1
        problem = int(log[1]) - 1
        time = int(log[2])
        result = log[3]

        if result == "CORRECT":
            data[team][1] += 1
            data[team][2] += wrong[team][problem] * 1200 + time
        else:
            wrong[team][problem] += 1

    data_sorted = sorted(data, key=lambda x: (-x[1], x[2], x[0]))

    for d in data_sorted:
        print(str(d[0]) + " " + str(d[1]) + " " + str(d[2]))