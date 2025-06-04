while True:
    line = input()
    if line == '0':
        break
    cards = list(map(int, line.split()))
    total = 0
    aces = 0
    for c in cards:
        if c == 1:
            aces += 1
            total += 1
        elif 2 <= c <= 9:
            total += c
        else:
            total += 10
    # Try to add 10 for some aces if it doesn't bust
    for _ in range(aces):
        if total + 10 <= 21:
            total += 10
    print(total if total <= 21 else 0)