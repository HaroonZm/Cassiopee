from itertools import permutations as P

def read_value():
    return int(input())

def should_stop(k):
    return k == 0

def read_n_k():
    n = read_value()
    k = read_value()
    return n, k

def read_card(n):
    return [read_value() for _ in range(n)]

def gen_permutations(card, k):
    return set(P(card, k))

def values_to_string(s):
    return ''.join(map(str, s))

def all_strings(perms):
    return [''.join(map(str, s)) for s in perms]

def unique_strings(strings):
    return set(strings)

def print_count(unique):
    print(len(unique))

def process(n, k, card):
    perms = gen_permutations(card, k)
    strings = all_strings(perms)
    unique = unique_strings(strings)
    print_count(unique)

def main_loop():
    while True:
        n, k = read_n_k()
        if should_stop(k):
            break
        card = read_card(n)
        process(n, k, card)

def main():
    main_loop()

main()