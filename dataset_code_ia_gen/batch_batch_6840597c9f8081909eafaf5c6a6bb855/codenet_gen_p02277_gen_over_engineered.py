class Card:
    __slots__ = ('suit', 'value', 'original_index')

    def __init__(self, suit: str, value: int, original_index: int):
        self.suit = suit
        self.value = value
        self.original_index = original_index

    def __le__(self, other: 'Card') -> bool:
        return self.value <= other.value

    def __repr__(self) -> str:
        return f"{self.suit} {self.value}"

class Comparator:
    def compare(self, a: Card, b: Card) -> bool:
        return a.value <= b.value

class PartitionStrategy:
    def partition(self, array: list, p: int, r: int, comparator: Comparator) -> int:
        x = array[r]
        i = p - 1
        for j in range(p, r):
            if comparator.compare(array[j], x):
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r] = array[r], array[i + 1]
        return i + 1

class QuickSortAlgorithm:
    def __init__(self, partition_strategy: PartitionStrategy, comparator: Comparator):
        self.partition_strategy = partition_strategy
        self.comparator = comparator

    def sort(self, array: list, p: int, r: int) -> None:
        if p < r:
            q = self.partition_strategy.partition(array, p, r, self.comparator)
            self.sort(array, p, q - 1)
            self.sort(array, q + 1, r)

class StabilityChecker:
    def __init__(self, original: list, sorted_: list):
        self.original = original
        self.sorted = sorted_

    def is_stable(self) -> bool:
        # Map from value to list of cards in original order 
        value_to_cards = {}
        for card in self.original:
            value_to_cards.setdefault(card.value, []).append(card)

        # Reconstruct the cards for each value as they appear in sorted list
        reconstructed_order = []
        for card in self.sorted:
            candidates = value_to_cards.get(card.value, [])
            if not candidates:
                return False
            # The first candidate must be the same card (same suit and original index)
            expected = candidates.pop(0)
            if expected.suit != card.suit or expected.original_index != card.original_index:
                return False
            reconstructed_order.append(expected)
        return True

class CardDeck:
    def __init__(self, cards: list):
        self.cards = cards

    def perform_sorting_and_check_stability(self):
        # Perform quick sort using the defined abstractions
        comparator = Comparator()
        partition_strategy = PartitionStrategy()
        quick_sort = QuickSortAlgorithm(partition_strategy, comparator)

        # Copy to keep original reference for stability checking
        original_cards = list(self.cards)

        quick_sort.sort(self.cards, 0, len(self.cards) - 1)

        stability_checker = StabilityChecker(original_cards, self.cards)
        stable = stability_checker.is_stable()

        return stable, self.cards

def main():
    import sys

    input_stream = sys.stdin
    n = int(input_stream.readline().strip())
    cards = []
    for i in range(n):
        suit, value_str = input_stream.readline().split()
        value = int(value_str)
        cards.append(Card(suit, value, i))

    deck = CardDeck(cards)
    stable, sorted_cards = deck.perform_sorting_and_check_stability()

    print("Stable" if stable else "Not stable")
    for card in sorted_cards:
        print(card)

if __name__=="__main__":
    main()