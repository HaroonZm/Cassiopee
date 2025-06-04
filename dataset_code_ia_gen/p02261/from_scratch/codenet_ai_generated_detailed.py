class Card:
    def __init__(self, suit_value, index):
        # suit_value is a string like 'H4', 'C9' etc.
        self.suit = suit_value[0]  # 'H', 'C', 'S' or 'D'
        self.value = int(suit_value[1:])  # numeric part converted to int
        self.original_index = index  # to track original order for stability checks
        self.string = suit_value  # original string representation for output

def bubble_sort(cards):
    n = len(cards)
    sorted_cards = cards[:]  # copy of the list to sort
    for i in range(n):
        for j in range(n-1, i, -1):
            # swap if value on right card is smaller
            if sorted_cards[j].value < sorted_cards[j-1].value:
                sorted_cards[j], sorted_cards[j-1] = sorted_cards[j-1], sorted_cards[j]
    return sorted_cards

def selection_sort(cards):
    n = len(cards)
    sorted_cards = cards[:]  # copy of the list to sort
    for i in range(n):
        mini = i
        for j in range(i, n):
            if sorted_cards[j].value < sorted_cards[mini].value:
                mini = j
        # swap i-th card with the card at mini
        sorted_cards[i], sorted_cards[mini] = sorted_cards[mini], sorted_cards[i]
    return sorted_cards

def is_stable(original_cards, sorted_cards):
    # A sorting is stable if cards of same value appear in same order as in original
    # We check by values: for any pair of values same in sorted list,
    # their relative order in the original must be preserved
    # To do so, we group indices in original_cards by value and see if order matches in sorted_cards
    
    from collections import defaultdict
    
    original_positions = defaultdict(list)
    for c in original_cards:
        # For each value store list of original indices in input order
        original_positions[c.value].append(c.original_index)
    
    # For sorted_cards we build the list of original indices by value in sorted order
    sorted_positions = defaultdict(list)
    for c in sorted_cards:
        sorted_positions[c.value].append(c.original_index)
    
    # Compare both lists per value, they must be identical for the sort to be stable
    for value in original_positions:
        if original_positions[value] != sorted_positions[value]:
            return False
    return True

def main():
    n = int(input())
    cards_input = input().split()
    
    # Create Card instances with original indices
    cards = [Card(cv, i) for i, cv in enumerate(cards_input)]
    
    # Perform Bubble Sort
    bubble_sorted = bubble_sort(cards)
    # Perform Selection Sort
    selection_sorted = selection_sort(cards)
    
    # Prepare output lines
    bubble_sorted_str = ' '.join(card.string for card in bubble_sorted)
    selection_sorted_str = ' '.join(card.string for card in selection_sorted)
    
    # Check stability for both sorting methods
    bubble_stable = "Stable" if is_stable(cards, bubble_sorted) else "Not stable"
    selection_stable = "Stable" if is_stable(cards, selection_sorted) else "Not stable"
    
    print(bubble_sorted_str)
    print(bubble_stable)
    print(selection_sorted_str)
    print(selection_stable)

if __name__ == "__main__":
    main()