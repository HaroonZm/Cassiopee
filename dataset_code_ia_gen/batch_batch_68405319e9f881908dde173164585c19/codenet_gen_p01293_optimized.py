rank_order = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
players = ['N','E','S','W']

while True:
    trump = input().strip()
    if trump == '#':
        break

    tricks_cards = [input().split() for _ in range(4)]  # 4 lines, each 13 cards
    # tricks_cards[player_index][trick_index]
    # We need cards per trick in the order N,E,S,W as given, which is already the rows.

    # transpose to get cards per trick in order N,E,S,W:
    tricks = list(zip(*tricks_cards))  # 13 tuples of 4 cards


    # The dealer was west, so first lead is north
    lead_index = 0  # N=0, E=1, S=2, W=3

    NS_tricks = 0
    EW_tricks = 0

    for trick in tricks:
        # order of play: starting from lead_index and next players clockwise
        order = [(lead_index + i)%4 for i in range(4)]
        cards_played = [trick[p] for p in order]
        # first card led
        led_suit = cards_played[0][1]

        # Determine winner of trick
        winning_pos = 0
        for i in range(1,4):
            c = cards_played[i]
            wc = cards_played[winning_pos]
            # If any trump played check trump else highest led_suit card
            # check if current winning card is trump
            wc_trump = (wc[1] == trump)
            c_trump = (c[1] == trump)

            if wc_trump:
                if c_trump and rank_order[c[0]] > rank_order[wc[0]]:
                    winning_pos = i
            else:
                if c_trump:
                    winning_pos = i
                else:
                    if c[1] == led_suit and wc[1] == led_suit and rank_order[c[0]] > rank_order[wc[0]]:
                        winning_pos = i
        winner = order[winning_pos]
        # update tricks count
        if winner%2==0:
            NS_tricks += 1
        else:
            EW_tricks += 1
        lead_index = winner

    if NS_tricks > EW_tricks:
        print("NS", NS_tricks - 6)
    else:
        print("EW", EW_tricks - 6)