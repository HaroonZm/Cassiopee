while True:
    deck = raw_input()
    if deck == '-':
        break
    else:
        m = int(raw_input())
        for i in range(m):
            h = int(raw_input())
            deck = deck[h:] + deck[:h]
        print deck