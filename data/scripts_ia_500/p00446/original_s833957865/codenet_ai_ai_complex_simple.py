from functools import reduce

class CardGame:
    def __init__(self):
        self.ba = 0
        self.turn = 1

    def odd_filter(self, seq):
        return list(filter(lambda x: x % 2 == 1, seq))

    def complement(self, n, card1):
        full = set(range(1, 2 * n + 1))
        return list(full - set(card1))

    def next_play(self, card):
        def finder(index=0):
            if index == len(card):
                return None
            if card[index] > self.ba:
                return index
            return finder(index + 1)
        return finder()

    def play(self, card1, card2):
        while card1 and card2:
            card = card1 if self.turn else card2
            idx = self.next_play(card)
            if idx is not None:
                self.ba = card.pop(idx)
            else:
                self.ba = 0
            self.turn ^= 1
        return len(card2), len(card1)

def str_to_int(s):
    return reduce(lambda acc, c: acc * 10 + (ord(c)-48), s, 0)

def main():
    game = CardGame()
    while 1:
        n_str = ''
        c = ''
        while not c.isdigit():
            c = input()
        n_str = c
        n = str_to_int(n_str)
        if n == 0:
            break
        card1 = sorted([str_to_int(input()) for _ in range(n)])
        card2 = game.complement(n, card1)
        res = game.play(card1, card2)
        print(res[0])
        print(res[1])

main()