ranks = "23456789TJQKA"
def rank_value(r): return ranks.index(r)
def winner(lead_suit, trumps, trick):
    trump_cards = [c for c in trick if c[1] == trumps]
    if trump_cards:
        return max((rank_value(c[0]), i) for i, c in enumerate(trick) if c[1] == trumps)[1]
    lead_cards = [c for c in trick if c[1] == lead_suit]
    return max((rank_value(c[0]), i) for i, c in enumerate(trick) if c[1] == lead_suit)[1]

positions = ['N', 'E', 'S', 'W']
while True:
    trumps = input().strip()
    if trumps == '#': break
    tricks = []
    for _ in range(13):
        line = input().strip().split()
        # each line: N,E,S,W cards for trick _
        # store by trick
        tricks.append(line)
    lead_pos = 0  # North leads first
    ns_wins = 0
    ew_wins = 0
    for trick in tricks:
        lead_suit = trick[lead_pos][1]
        i = winner(lead_suit, trumps, trick)
        lead_pos = i
        if positions[i] in ['N','S']: ns_wins += 1
        else: ew_wins +=1
    if ns_wins > ew_wins:
        print("NS", ns_wins - 6)
    else:
        print("EW", ew_wins - 6)