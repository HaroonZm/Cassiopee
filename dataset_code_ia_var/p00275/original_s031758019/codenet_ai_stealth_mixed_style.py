proceed=True
while proceed:
    try:
        N=int(input())
        if N==0:
            proceed=False; continue
        dataset = input()
        from collections import defaultdict
        mens = ['']*N
        idx = 0
        p = ''
        def process(card, ix):
            nonlocal p
            if card == 'M':
                mens[ix] += card
            elif card == 'S':
                tmp = p
                p = ''
                p += card+mens[ix]
                mens[ix] = ''
            else:
                mens[ix] += card+p
                p=''
        for c in dataset:
            if idx>=N:
                idx=0
            process(c, idx)
            idx+=1
        # comprehension et lambda pour mélange de style
        print(*sorted(list(map(lambda x:len(x), mens))), len(p))
    except:
        break