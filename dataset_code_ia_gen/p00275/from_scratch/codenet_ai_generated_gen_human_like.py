while True:
    N = int(input())
    if N == 0:
        break
    cards = input().strip()

    players = [0] * N
    table = 0
    turn = 0

    for c in cards:
        if c == 'M':
            players[turn] += 1
        elif c == 'S':
            # Player puts all cards including S on the table
            table += players[turn] + 1
            players[turn] = 0
        else:  # c == 'L'
            # Player gets all cards on the table including L card
            players[turn] += table + 1
            table = 0
        turn = (turn + 1) % N

    players.sort()
    players.append(table)
    print(" ".join(map(str, players)))