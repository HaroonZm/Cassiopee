import sys
input_lines = []
for input_line in sys.stdin:
    input_line = input_line.rstrip()
    input_lines.append(input_line)

for input_pair_index in range(len(input_lines) // 2):
    card_count, round_count = map(int, input_lines[2 * input_pair_index].split())
    operation_counts = list(map(int, input_lines[2 * input_pair_index + 1].split()))
    deck = [card_index for card_index in range(card_count)]
    for operation_count in operation_counts:
        half_deck_1 = deck[card_count // 2:card_count]
        half_deck_2 = deck[0:card_count // 2]
        mixed_deck = []
        while len(half_deck_1) > 0 or len(half_deck_2) > 0:
            take_from_half_1 = half_deck_1[:operation_count]
            half_deck_1 = half_deck_1[operation_count:]
            mixed_deck += take_from_half_1

            take_from_half_2 = half_deck_2[:operation_count]
            half_deck_2 = half_deck_2[operation_count:]
            mixed_deck += take_from_half_2
        deck = mixed_deck
    print(deck[-1])