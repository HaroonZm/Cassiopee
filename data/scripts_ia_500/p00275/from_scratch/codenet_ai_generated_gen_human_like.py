while True:
    N = int(input())
    if N == 0:
        break
    cards = input().strip()

    players = [[] for _ in range(N)]
    field = []
    for i, c in enumerate(cards):
        player = i % N
        if c == 'M':
            players[player].append(c)
        elif c == 'S':
            # remove all cards from the player including this one to the field
            field.extend(players[player])
            players[player].clear()
            field.append(c)
        else:  # c == 'L'
            # player takes this card and all cards on the field
            players[player].append(c)
            players[player].extend(field)
            field.clear()

    counts = [len(p) for p in players]
    counts.sort()
    counts.append(len(field))
    print(*counts)