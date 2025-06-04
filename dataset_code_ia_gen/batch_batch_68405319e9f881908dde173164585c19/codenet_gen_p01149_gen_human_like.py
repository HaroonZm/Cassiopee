def card_value(card):
    if card in ['T', 'J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

def hand_score(cards):
    total = 0
    aces = 0
    for card in cards:
        val = card_value(card)
        total += val
        if card == 'A':
            aces += 1
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total, aces

def is_blackjack(cards):
    if len(cards) != 2:
        return False
    a, b = cards
    if 'A' in cards and (b in ['T', 'J', 'Q', 'K', 'T'] or a in ['T', 'J', 'Q', 'K', 'T']):
        return True
    return False

def dealer_play(dealer_cards, pile):
    # Check for dealer blackjack initially
    if is_blackjack(dealer_cards):
        return "blackjack"
    score, aces = hand_score(dealer_cards)
    if score > 21:
        return "bust"
    # Dealer hits according to rules
    i = 0
    while True:
        # dealer hits on 16 or less
        # hits on soft 17 (17 with an ace counted as 11)
        if score < 17:
            if i >= len(pile):
                break
            dealer_cards.append(pile[i])
            i += 1
            score, aces = hand_score(dealer_cards)
            if score > 21:
                return "bust"
        elif score == 17 and aces > 0:
            # soft 17, hit
            if i >= len(pile):
                break
            dealer_cards.append(pile[i])
            i += 1
            score, aces = hand_score(dealer_cards)
            if score > 21:
                return "bust"
        else:
            # stands otherwise
            break
    return str(score)

def main():
    N = int(input())
    for _ in range(N):
        dealer_cards = input().strip().split()
        pile = input().strip().split()
        print(dealer_play(dealer_cards, pile))

if __name__ == "__main__":
    main()