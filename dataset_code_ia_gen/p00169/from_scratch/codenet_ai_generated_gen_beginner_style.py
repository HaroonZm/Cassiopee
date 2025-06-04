while True:
    line = input()
    if line == '0':
        break
    cards = list(map(int, line.split()))
    total = 0
    num_ones = 0
    for c in cards:
        if c == 1:
            num_ones += 1
            total += 1
        elif 2 <= c <= 9:
            total += c
        else:
            total += 10
    # essayer avec les uns comptés comme 11 quand possible
    for _ in range(num_ones):
        if total + 10 <= 21:
            total += 10
    if total > 21:
        total = 0
    print(total)