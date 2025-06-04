n = int(input())
for _ in range(n):
    bases = [False, False, False]  # first, second, third base
    score = 0
    outs = 0
    while outs < 3:
        try:
            event = input().strip()
        except EOFError:
            break
        if event == '':
            break
        if event == "HIT":
            # advance runners
            if bases[2]:
                score += 1
            bases[2] = bases[1]
            bases[1] = bases[0]
            bases[0] = True
        elif event == "HOMERUN":
            # score all runners + 1
            score += sum(bases) + 1
            bases = [False, False, False]
        elif event == "OUT":
            outs += 1
        if outs == 3:
            # inning ends
            # break only if no more input or next line empty?
            pass
    print(score)