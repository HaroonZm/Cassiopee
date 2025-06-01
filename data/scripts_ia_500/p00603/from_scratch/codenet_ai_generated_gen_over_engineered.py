from collections import deque
from typing import List, Iterable, Iterator

class Deck:
    def __init__(self, cards: Iterable[int]):
        self.cards = deque(cards)

    def split(self) -> ('Deck', 'Deck'):
        mid = (len(self.cards) + 1) // 2
        # Top half is deck A, bottom half deck B.
        # But deck is represented bottom->top, so splitting by slicing:
        # bottom cards 0..mid-1 belong to deck A (top half)
        # cards mid..end belong to deck B (bottom half)
        # Actually from problem: deck A is top half, deck B bottom half
        # Since bottom of deck is left of deque: cards[0] bottom, cards[-1] top
        # So deck A = top half means deck A is cards[-mid:] (top cards)
        # deck B = bottom half means cards[:-mid]
        a_cards = list(self.cards)[-mid:]
        b_cards = list(self.cards)[:-mid]
        return Deck(a_cards), Deck(b_cards)

    def take_from_bottom(self, c: int) -> List[int]:
        count = min(c, len(self.cards))
        taken = [self.cards.popleft() for _ in range(count)]
        return taken

    def add_to_top(self, cards: List[int]):
        # Add cards on top of deck
        for card in cards:
            self.cards.append(card)

    def is_empty(self) -> bool:
        return not self.cards

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck({list(self.cards)})"

class RiffleShuffler:
    def __init__(self, n: int):
        # create initial deck numbered 0..n-1 from bottom to top (left to right in deque)
        self.deck = Deck(range(n))

    def single_riffle(self, c: int):
        # split deck into A (top half) and B (bottom half)
        deck_a, deck_b = self.deck.split()
        deck_c = Deck([])

        # repeatedly take c cards from bottom of deck A and B and add them to deck C top
        # but stacking onto deck C means adding at top, so append at right in deque

        # we will pull cards from deck_a and deck_b bottom (popleft), add to deck_c top (append)
        while not deck_a.is_empty() or not deck_b.is_empty():
            if not deck_a.is_empty():
                taken_a = deck_a.take_from_bottom(c)
                deck_c.add_to_top(taken_a)
            if not deck_b.is_empty():
                taken_b = deck_b.take_from_bottom(c)
                deck_c.add_to_top(taken_b)

        self.deck = deck_c

    def perform_riffles(self, operations: Iterable[int]):
        for c in operations:
            self.single_riffle(c)

    def top_card(self) -> int:
        # top card at top of deck, i.e. rightmost element of deque
        return self.deck.cards[-1]

class InputProcessor:
    def __init__(self):
        pass

    def parse(self, lines: Iterator[str]) -> Iterator[tuple[int,int,List[int]]]:
        for line in lines:
            if not line.strip():
                continue
            try:
                n,r = map(int, line.strip().split())
            except ValueError:
                # maybe EOF encountered
                break
            ops = []
            while len(ops) < r:
                ops_line = next(lines).strip()
                if ops_line == '':
                    continue
                ops.extend(map(int, ops_line.split()))
            yield n, r, ops

def main():
    import sys
    processor = InputProcessor()
    lines = iter(sys.stdin.readline, '')
    for n, r, ops in processor.parse(lines):
        shuffler = RiffleShuffler(n)
        shuffler.perform_riffles(ops)
        print(shuffler.top_card())

if __name__ == "__main__":
    main()