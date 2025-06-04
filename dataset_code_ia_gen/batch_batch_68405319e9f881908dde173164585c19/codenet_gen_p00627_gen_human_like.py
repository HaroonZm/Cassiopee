while True:
    n = int(input())
    if n == 0:
        break
    total_hits = 0
    rounds = n // 4
    for _ in range(rounds):
        total_hits += int(input())
    print(total_hits)