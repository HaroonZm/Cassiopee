def read_int():
    return int(input())

def initialize_cards(n):
    return list(range(1, 2*n+1))

def split_cards(card, n):
    return card[:n], card[n:]

def interleave_cards(card1, card2):
    result = []
    for c1, c2 in zip(card1, card2):
        result.append(c1)
        result.append(c2)
    return result

def cut_cards(card, ope):
    card1 = card[:ope]
    card2 = card[ope:]
    return card2 + card1

def process_operation(card, n, ope):
    if ope == 0:
        card1, card2 = split_cards(card, n)
        card = interleave_cards(card1, card2)
    else:
        card = cut_cards(card, ope)
    return card

def print_cards(card):
    for c in card:
        print(c)

def main():
    n = read_int()
    m = read_int()
    card = initialize_cards(n)
    for _ in range(m):
        ope = read_int()
        card = process_operation(card, n, ope)
    print_cards(card)

main()