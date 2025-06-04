import sys

def shuffle_deck(deck_input, chunk_size):
    deck_length = len(deck_input)
    split_index = deck_length // 2 if deck_length % 2 == 0 else (deck_length - 1) // 2
    upper_half = deck_input[split_index:]
    lower_half = deck_input[:split_index]
    merged_deck = []
    while upper_half or lower_half:
        merged_deck.extend(upper_half[:chunk_size])
        upper_half = upper_half[chunk_size:]
        merged_deck.extend(lower_half[:chunk_size])
        lower_half = lower_half[chunk_size:]
    return merged_deck

while True:
    input_line = sys.stdin.readline()
    if not input_line:
        break
    num_cards, num_rounds = map(int, input_line.strip().split())
    initial_deck = [index for index in range(num_cards)]
    chunk_size_list = map(int, sys.stdin.readline().strip().split())
    current_deck = initial_deck
    for chunk_size in chunk_size_list:
        current_deck = shuffle_deck(current_deck, chunk_size)
    print(current_deck[-1])