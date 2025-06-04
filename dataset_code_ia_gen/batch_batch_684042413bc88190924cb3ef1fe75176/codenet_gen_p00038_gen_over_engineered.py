from collections import Counter
from typing import List, Dict, Tuple, Callable, Optional

class Card:
    """Représente une carte de poker avec une valeur numérique."""
    def __init__(self, value: int):
        if not (1 <= value <= 13):
            raise ValueError("La valeur de la carte doit être entre 1 et 13 inclus.")
        self.value = value

    def __repr__(self):
        return f"Card({self.value})"

class Hand:
    """Représente une main de poker de 5 cartes."""
    def __init__(self, cards: List[Card]):
        if len(cards) != 5:
            raise ValueError("Une main doit contenir exactement 5 cartes.")
        self.cards = cards
        self.values = sorted(card.value for card in cards)
        self.counts = Counter(self.values)

    def is_straight(self) -> bool:
        # Cas normal (suite classique)
        sorted_values = sorted(set(self.values))
        if len(sorted_values) != 5:
            return False
        # note: les valeurs sont 1..13 avec 1 = As
        # On considère deux possibilités pour l'as dans la suite:
        # A 2 3 4 5 ou 10 J Q K A (où A est 1)
        # Donc:
        # 1) vérifier si max-min=4 et que les valeurs sont consécutives
        if sorted_values[-1] - sorted_values[0] == 4:
            return True
        # 2) vérifier si c'est la suite A,10,11,12,13 (A à la fin)
        if sorted_values == [1,10,11,12,13]:
            return True
        return False

    def classify(self) -> str:
        """Détermine le rang de la main selon les règles données."""
        count_values = list(self.counts.values())
        unique_vals = len(self.counts)

        # Vérifier Four of a kind
        if 4 in count_values:
            return "four card"
        # Full house
        if 3 in count_values and 2 in count_values:
            return "full house"
        # Straight
        if self.is_straight():
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
        # Aucun rôle
        return "null"

class PokerHandParser:
    """Parser statique pour transformer une ligne d'entrée en main de poker."""
    @staticmethod
    def parse_line(line: str) -> Hand:
        parts = line.strip().split(",")
        if len(parts) != 5:
            raise ValueError("Chaque main doit contenir 5 cartes.")
        cards = [Card(int(x)) for x in parts]
        return Hand(cards)

class PokerEvaluator:
    """Classe d'évaluation des mains, anticipant extension future."""
    def __init__(self, hands: List[Hand]):
        self.hands = hands

    def evaluate(self) -> List[str]:
        results = []
        for hand in self.hands:
            results.append(hand.classify())
        return results

def main():
    import sys
    lines = []
    for line in sys.stdin:
        if not line.strip():
            continue
        lines.append(line.strip())
    hands = [PokerHandParser.parse_line(ln) for ln in lines]
    evaluator = PokerEvaluator(hands)
    results = evaluator.evaluate()
    for res in results:
        print(res)

if __name__ == "__main__":
    main()