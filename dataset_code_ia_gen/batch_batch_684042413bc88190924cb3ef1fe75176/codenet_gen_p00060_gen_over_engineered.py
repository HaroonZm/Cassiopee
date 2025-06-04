from abc import ABC, abstractmethod
from typing import List, Set, Optional, Iterator

class Card:
    __slots__ = ['value']
    def __init__(self, value: int):
        if not 1 <= value <= 10:
            raise ValueError("Card value must be between 1 and 10 inclusive.")
        self.value = value
    def __repr__(self):
        return f"Card({self.value})"
    def __eq__(self, other):
        return isinstance(other, Card) and self.value == other.value
    def __hash__(self):
        return hash(self.value)

class Deck:
    def __init__(self):
        self._cards: Set[Card] = set(Card(v) for v in range(1, 11))
    def remove_cards(self, cards: List[Card]) -> None:
        for card in cards:
            self._cards.discard(card)
    def available_cards(self) -> Set[Card]:
        return set(self._cards)

class Hand(ABC):
    @abstractmethod
    def cards(self) -> List[Card]:
        pass
    def total_value(self) -> int:
        return sum(card.value for card in self.cards())
    def __repr__(self):
        return f"{self.__class__.__name__}({self.cards()})"

class PlayerHand(Hand):
    def __init__(self, cards: List[Card]):
        if len(cards) != 2:
            raise ValueError("PlayerHand must be initialized with exactly 2 cards")
        self._cards = cards
    def cards(self) -> List[Card]:
        return self._cards

class OpponentHand(Hand):
    def __init__(self, visible_card: Card, hidden_card: Optional[Card] = None):
        self._visible = visible_card
        self._hidden = hidden_card
    def set_hidden(self, hidden_card: Card) -> None:
        self._hidden = hidden_card
    def cards(self) -> List[Card]:
        if self._hidden is None:
            return [self._visible]
        return [self._visible, self._hidden]
    def visible_card(self) -> Card:
        return self._visible

class ProbabilityCalculator:
    def __init__(self, deck: Deck):
        self.deck = deck
    def probability_sum_no_exceed(self, base_cards: List[Card], threshold: int) -> float:
        """Calculate probability that sum(base_cards + one extra card) ≤ threshold"""
        base_sum = sum(card.value for card in base_cards)
        available_cards = self.deck.available_cards()
        # Exclude base cards already in use (3 known cards)
        cards_used = set(base_cards)
        candidate_cards = available_cards - cards_used
        if not candidate_cards:
            # No cards left to draw, probability is zero if sum already > threshold, else 1
            return 1.0 if base_sum <= threshold else 0.0
        successful = 0
        total = len(candidate_cards)
        for card in candidate_cards:
            if base_sum + card.value <= threshold:
                successful += 1
        return successful / total

class InputParser:
    def __init__(self, source: Iterator[str]):
        self.source = source
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            line = next(self.source)
            if line.strip() == '':
                continue
            parts = line.strip().split()
            if len(parts) != 3:
                raise ValueError("Each input line must contain exactly three integers.")
            c1, c2, c3 = map(int, parts)
            return c1, c2, c3

class GameLogic:
    SUM_LIMIT = 20
    THRESHOLD_PROBABILITY = 0.5
    def __init__(self):
        self.deck = Deck()
    def decide_draw(self, c1: int, c2: int, c3: int) -> str:
        # Setup cards
        player_cards = [Card(c1), Card(c2)]
        opponent_visible = Card(c3)
        # Remove known cards from deck
        self.deck = Deck()  # fresh deck
        self.deck.remove_cards(player_cards + [opponent_visible])
        player_hand = PlayerHand(player_cards)
        # Calculate probability for player's own hand
        prob_player = ProbabilityCalculator(self.deck).probability_sum_no_exceed(player_hand.cards(), self.SUM_LIMIT)
        # Calculate probability for opponent's visible card only (since hidden unknown)
        # Opponent can only draw one card, but we must test as per problem statement for all three cards
        # So we apply the probability calc for each card in input (that's c1, c2, c3)
        # But problem wants output per line, so here we just solve per input line.
        # So output YES if prob_player >= 0.5 else NO
        return "YES" if prob_player >= self.THRESHOLD_PROBABILITY else "NO"

def main() -> None:
    import sys
    parser = InputParser(iter(sys.stdin))
    game = GameLogic()
    try:
        while True:
            c1, c2, c3 = next(parser)
            print(game.decide_draw(c1, c2, c3))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()