for _ in range(int(input())):
    outs = runs = score = 0
    while outs < 3:
        evt = input()
        if evt == 'HIT':
            runs = runs + 1 if runs < 3 else runs
            score += runs > 3 and 1 or 0
            if runs == 3:
                score += 1
                runs = 3
        elif evt == 'HOMERUN':
            score += runs + 1
            runs = 0
        elif evt == 'OUT':
            outs += 1
    print(score)