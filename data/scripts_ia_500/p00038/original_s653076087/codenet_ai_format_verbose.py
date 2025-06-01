import collections

def evaluate_hand(sorted_cards, sorted_card_counts):
    
    highest_count = sorted_card_counts[0][1]
    
    if highest_count == 4:
        return "four card"
    
    if highest_count == 3:
        if sorted_card_counts[1][1] == 2:
            return "full house"
        else:
            return "three card"
    
    if highest_count == 2:
        if sorted_card_counts[1][1] == 2:
            return "two pair"
        else:
            return "one pair"
    
    is_ace_low_straight = (
        sorted_cards[0] == 1 and
        list(range(10, 14)) == sorted_cards[1:]
    )
    
    is_consecutive_straight = (
        list(range(sorted_cards[0], sorted_cards[0] + 5)) == sorted_cards
    )
    
    if is_ace_low_straight or is_consecutive_straight:
        return "straight"
    
    return "null"


while True:
    try:
        input_cards = input().split(",")
        integer_cards = list(map(int, input_cards))
    except Exception:
        break

    sorted_cards = sorted(integer_cards)
    
    card_count = collections.Counter(integer_cards)
    
    sorted_card_counts = sorted(card_count.items(), key=lambda item: -item[1])
    
    result = evaluate_hand(sorted_cards, sorted_card_counts)
    
    print(result)