for _ in range(int(input())):
    outs = hits = points = 0
    while outs < 3:
        event = input()
        if event == "OUT":
            outs += 1
        elif event == "HIT":
            hits += 1
        elif event == "HOMERUN":
            points += hits + 1
            hits = 0
    points += max(0, hits - 3)
    print(points)