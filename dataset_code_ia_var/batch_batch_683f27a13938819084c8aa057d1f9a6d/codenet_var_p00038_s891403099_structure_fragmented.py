def get_raw_hand():
    return input().split(",")

def init_hand_list():
    return [0] * 14

def map_card_to_index(card):
    if card == "A":
        return 1
    elif card == "J":
        return 11
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    else:
        return int(card)

def count_cards(raw_hand):
    hand = init_hand_list()
    for card in raw_hand:
        idx = map_card_to_index(card)
        hand[idx] += 1
    return hand

def analyze_ranks(hand):
    pairs = 0
    three = False
    four = False
    minone = 0
    found_minone = False
    for i in range(14):
        ranks = hand[i]
        if ranks == 1 and not found_minone:
            minone = i
            found_minone = True
        elif ranks == 2:
            pairs += 1
        elif ranks == 3:
            three = True
        elif ranks == 4:
            four = True
            break
    return pairs, three, four, minone, found_minone

def is_normal_straight(hand, minone, found_minone):
    if not found_minone:
        return False
    for offset in range(5):
        if minone + offset > 13 or hand[minone + offset] != 1:
            return False
    return True

def is_ace_high_straight(hand):
    return hand[1]==1 and hand[10]==1 and hand[11]==1 and hand[12]==1 and hand[13]==1

def check_straight(hand, minone, found_minone):
    if is_normal_straight(hand, minone, found_minone):
        return True
    if is_ace_high_straight(hand):
        return True
    return False

def classify_hand(four, three, pairs, straight):
    if four:
        return "four card"
    elif three and pairs == 1:
        return "full house"
    elif straight:
        return "straight"
    elif three:
        return "three card"
    elif pairs == 2:
        return "two pair"
    elif pairs == 1:
        return "one pair"
    else:
        return "null"

def process_hand():
    raw_hand = get_raw_hand()
    hand = count_cards(raw_hand)
    pairs, three, four, minone, found_minone = analyze_ranks(hand)
    straight = check_straight(hand, minone, found_minone)
    result = classify_hand(four, three, pairs, straight)
    print(result)

def poker_main_loop():
    while True:
        try:
            process_hand()
        except EOFError:
            break

poker_main_loop()