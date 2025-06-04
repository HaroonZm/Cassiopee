while 1:
    a = [list(map(int, input())) for _ in [0] * 8]
    y = [sum(r) for r in a]
    x = [sum(c) for c in zip(*a)]
    print(
        'B' if 4 in x else
        'C' if 4 in y else
        'DF'[a[y.index(1)][x.index(2)]] if 1 in y else
        'GE'[a[y.index(2)][x.index(1)]] if 1 in x else
        'A'
    )
    try:
        input()
    except:
        break