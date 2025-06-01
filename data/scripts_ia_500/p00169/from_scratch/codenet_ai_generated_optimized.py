while True:
    line = input().strip()
    if line == '0':
        break
    cards = list(map(int, line.split()))
    total = 0
    ace_count = 0
    for c in cards:
        if c == 1:
            ace_count += 1
            total += 1
        elif 2 <= c <= 9:
            total += c
        else:
            total += 10
    # Essayons de convertir certains As en 11 points tant que la somme <=21
    for _ in range(ace_count):
        if total + 10 <= 21:
            total += 10
    print(total if total <= 21 else 0)