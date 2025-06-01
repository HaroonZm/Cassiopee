import sys
import os

def setup_input():
    if os.environ.get('PYDEV') == "True":
        sys.stdin = open("sample-input.txt", "rt")

def parse_line(line):
    return [int(x) for x in line.split()]

def generate_all_cards():
    return list(range(1, 11))

def remove_used_cards(all_cards, used_cards):
    for card in used_cards:
        all_cards.remove(card)
    return all_cards

def compute_sum_of_two_cards(card1, card2):
    return card1 + card2

def count_cards_fitting_condition(cards, partial_sum):
    count = 0
    for card in cards:
        if is_sum_with_card_valid(partial_sum, card):
            count += 1
    return count

def is_sum_with_card_valid(partial_sum, card):
    return partial_sum + card <= 20

def is_card_count_greater_than_threshold(count, threshold=3):
    return count > threshold

def card_game(c1, c2, c3):
    all_cards = generate_all_cards()
    remaining_cards = remove_used_cards(all_cards, [c1, c2, c3])
    partial_sum = compute_sum_of_two_cards(c1, c2)
    valid_count = count_cards_fitting_condition(remaining_cards, partial_sum)
    return is_card_count_greater_than_threshold(valid_count)

def print_result(result):
    if result:
        print("YES")
    else:
        print("NO")

def main():
    setup_input()
    for line in sys.stdin:
        c1, c2, c3 = parse_line(line)
        result = card_game(c1, c2, c3)
        print_result(result)

main()