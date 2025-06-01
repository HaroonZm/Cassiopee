import sys
from collections import Counter

def is_straight(vals):
    vals_set = set(vals)
    if len(vals_set) != 5:
        return False
    sorted_vals = sorted(vals)
    # Check normal straight
    if sorted_vals[4] - sorted_vals[0] == 4:
        return True
    # Check straight with A as 14 (A 2 3 4 5)
    if set([1,2,3,4,5]) == vals_set:
        return True
    # Check straight with A as high (10 J Q K A)
    if set([10,11,12,13,1]) == vals_set:
        return True
    return False

def rank_hand(cards):
    counts = Counter(cards)
    count_values = sorted(counts.values(), reverse=True)
    # Four card
    if 4 in count_values:
        return "four card"
    # Full house
    if count_values == [3,2]:
        return "full house"
    # Straight
    if is_straight(cards):
        return "straight"
    # Three card
    if 3 in count_values:
        return "three card"
    # Two pair
    if count_values.count(2) == 2:
        return "two pair"
    # One pair
    if 2 in count_values:
        return "one pair"
    return "null"

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    cards = list(map(int,line.split(',')))
    print(rank_hand(cards))