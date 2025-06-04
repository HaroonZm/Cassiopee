while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    winners = []
    for _ in range(n):
        pattern, prize = input().split()
        prize = int(prize)
        winners.append((pattern, prize))

    tickets = [input() for _ in range(m)]

    total_prize = 0
    for ticket in tickets:
        for pattern, prize in winners:
            match = True
            for i in range(8):
                if pattern[i] != '*' and pattern[i] != ticket[i]:
                    match = False
                    break
            if match:
                total_prize += prize
                break

    print(total_prize)