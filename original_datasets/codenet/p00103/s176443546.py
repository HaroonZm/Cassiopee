n = int(input())
for _ in range(n):
    n_out, n_run, score = 0, 0, 0
    while n_out < 3:
        evt = input()
        if evt == 'HIT':
            if n_run < 3:
                n_run += 1
            else:
                score += 1
        elif evt == 'HOMERUN':
            score += n_run + 1
            n_run = 0
        elif evt == 'OUT':
            n_out += 1
    print(score)