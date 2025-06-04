import sys

def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    cards = []
    for i in range(1, 2 * n + 1):
        cards.append(i)
    for i in range(m):
        op = int(sys.stdin.readline())
        if op == 0:
            # Shuffle
            new_cards = []
            for j in range(n):
                new_cards.append(cards[j])
                new_cards.append(cards[j + n])
            cards = new_cards
        else:
            # Cut
            cut_cards = []
            for j in range(op, 2 * n):
                cut_cards.append(cards[j])
            for j in range(op):
                cut_cards.append(cards[j])
            cards = cut_cards
    for card in cards:
        print(card)

if __name__ == '__main__':
    main()