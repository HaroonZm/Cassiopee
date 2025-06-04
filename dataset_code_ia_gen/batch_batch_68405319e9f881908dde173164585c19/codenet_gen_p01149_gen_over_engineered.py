class Card:
    _rank_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, 'T': 10,
        'J': 10, 'Q': 10, 'K': 10,
        'A': 11
    }

    def __init__(self, rank):
        self.rank = rank

    @property
    def value(self):
        return self._rank_values[self.rank]

    @property
    def is_ace(self):
        return self.rank == 'A'


class Hand:
    def __init__(self, cards=None):
        self.cards = cards if cards else []

    def add_card(self, card):
        self.cards.append(card)

    def values(self):
        total = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.is_ace)
        # Adjust aces from 11 to 1 while total > 21
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total

    def soft_17(self):
        # Soft 17 means total 17 with one ace counted as 11
        total = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.is_ace)
        # if total == 17 and at least one ace still counted as 11
        while aces > 0:
            if total == 17:
                return True
            total -= 10
            aces -= 1
        return False

    def is_blackjack(self):
        # Blackjack is exactly two cards: an ace and a ten-value card
        if len(self.cards) != 2:
            return False
        ranks = [card.rank for card in self.cards]
        return ('A' in ranks) and any(r in ranks for r in ['T', 'J', 'Q', 'K'])

    def is_bust(self):
        return self.values() > 21


class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.position = 0

    def draw(self):
        if self.position >= len(self.cards):
            raise RuntimeError("No more cards to draw")
        card = Card(self.cards[self.position])
        self.position += 1
        return card


class Dealer:
    def __init__(self, initial_cards, draw_pile_cards):
        self.hand = Hand([Card(c) for c in initial_cards])
        self.draw_pile = Deck(draw_pile_cards)

    def play(self):
        # Check initial blackjack
        if self.hand.is_blackjack():
            return "blackjack"

        # Play according to rules:
        # Hits if score <=16 or soft 17
        while True:
            score = self.hand.values()
            if score < 17:
                self.hand.add_card(self.draw_pile.draw())
            elif score == 17 and self.hand.soft_17():
                self.hand.add_card(self.draw_pile.draw())
            else:
                break

        if self.hand.is_bust():
            return "bust"
        else:
            return str(self.hand.values())


class BlackjackGameSimulator:
    def __init__(self, test_cases):
        # test_cases: list of tuples (initial_cards, draw_pile_cards)
        self.test_cases = test_cases

    def simulate(self):
        results = []
        for initial_cards, draw_pile_cards in self.test_cases:
            dealer = Dealer(initial_cards, draw_pile_cards)
            results.append(dealer.play())
        return results


def parse_input():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    N = int(input_lines[0])
    test_cases = []
    idx = 1
    for _ in range(N):
        initial_cards = input_lines[idx].split()
        draw_pile_cards = input_lines[idx+1].split()
        idx += 2
        test_cases.append((initial_cards, draw_pile_cards))
    return test_cases


def main():
    test_cases = parse_input()
    simulator = BlackjackGameSimulator(test_cases)
    results = simulator.simulate()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()