while True:
    N = int(input())
    if N == 0:
        break

    knowledge = [set() for _ in range(N+1)]
    for i in range(1, N+1):
        data = list(map(int, input().split()))
        M = data[0]
        if M > 0:
            knowledge[i].update(data[1:])

    data = list(map(int, input().split()))
    K = data[0]
    leaked = set(data[1:])

    possible_suspects = []
    for suspect in range(1, N+1):
        # suspect must be able to know at least all leaked members
        if not leaked.issubset(knowledge[suspect]):
            continue

        # we simulate that suspect leaked exactly these members.
        # Check if this assumption leads to contradiction:
        # Nobody else can have leaked any member outside leaked set.
        # Also, anyone in leaked set must be known by suspect.
        contradiction = False
        for member in range(1, N+1):
            if member == suspect:
                continue
            # member's known set should not contain anyone outside leaked,
            # because leaked info did not leak that info
            if not knowledge[member].issubset(leaked):
                contradiction = True
                break
        if contradiction:
            continue
        possible_suspects.append(suspect)

    if len(possible_suspects) == 1:
        print(possible_suspects[0])
    else:
        print(-1)