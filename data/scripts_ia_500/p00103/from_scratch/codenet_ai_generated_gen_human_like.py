n = int(input())
for _ in range(n):
    score = 0
    outs = 0
    bases = [False, False, False]  # first, second, third base
    while outs < 3:
        try:
            event = input()
        except EOFError:
            break
        if event == "HIT":
            # Advance runners and put new runner on first base
            if bases[2]:
                score += 1
            bases[2] = bases[1]
            bases[1] = bases[0]
            bases[0] = True
        elif event == "HOMERUN":
            # Score runs for all runners plus batter
            score += sum(bases) + 1
            bases = [False, False, False]
        elif event == "OUT":
            outs += 1
        if outs == 3:
            break
    print(score)