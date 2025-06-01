from itertools import permutations as perm_iter

while True:
    number_of_cards = int(input())
    pick_count = int(input())
    if pick_count == 0:
        break
    card_values = [int(input()) for _ in range(number_of_cards)]
    unique_permutation_strings = set(
        ''.join(map(str, perm))
        for perm in set(perm_iter(card_values, pick_count))
    )
    unique_permutation_count = len(unique_permutation_strings)
    print(unique_permutation_count)