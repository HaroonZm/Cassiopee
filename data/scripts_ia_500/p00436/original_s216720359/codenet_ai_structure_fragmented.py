import sys
from sys import stdin
from itertools import chain

input = stdin.readline

def flatten(list_of_lists):
    return chain.from_iterable(list_of_lists)

def get_n():
    return int(input())

def get_m():
    return int(input())

def initialize_cards(n):
    return [x for x in range(1, (2 * n) + 1)]

def read_operation():
    return int(input())

def split_cards(cards, n):
    return cards[:n], cards[n:]

def interleave_lists(list1, list2):
    return list(flatten([[a, b] for a, b in zip(list1, list2)]))

def perform_shuffle(cards, n):
    yellow, blue = split_cards(cards, n)
    return interleave_lists(yellow, blue)

def perform_cut(cards, k):
    return cards[k:] + cards[:k]

def process_operation(cards, n, op):
    if op == 0:
        return perform_shuffle(cards, n)
    else:
        return perform_cut(cards, op)

def print_cards(cards):
    print('\n'.join(map(str, cards)))

def main(args):
    n = get_n()
    m = get_m()
    cards = initialize_cards(n)
    for _ in range(m):
        op = read_operation()
        cards = process_operation(cards, n, op)
    print_cards(cards)

if __name__ == '__main__':
    main(sys.argv[1:])