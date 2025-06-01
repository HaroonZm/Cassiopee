while True:
    N = int(input())
    if N == 0:
        break
    data = input()
    players = ["" for _ in range(N)]
    index = 0
    pile = ""
    
    while data:
        if index == N:
            index = 0
        card = data[0]
        data = data[1:]
        
        if card == "M":
            players[index] += card
        elif card == "S":
            pile += card + players[index]
            players[index] = ""
        else:
            players[index] += card + pile
            pile = ""
        index += 1
    
    # Sorting by length, because I guess that's what matters here
    lengths = sorted([len(p) for p in players])
    print(' '.join(str(l) for l in lengths), len(pile))