import sys

from bisect import bisect_right

def play_card_game(taro_cards_sorted, hanako_cards_sorted):
    current_pile_card = taro_cards_sorted.pop(0)
    current_player_cards = hanako_cards_sorted

    while taro_cards_sorted and hanako_cards_sorted:
        position_to_play = bisect_right(current_player_cards, current_pile_card)

        if position_to_play != len(current_player_cards):
            current_pile_card = current_player_cards.pop(position_to_play)
        else:
            if current_player_cards is hanako_cards_sorted:
                current_player_cards = taro_cards_sorted
            else:
                current_player_cards = hanako_cards_sorted
            current_pile_card = current_player_cards.pop(0)
        if current_player_cards is hanako_cards_sorted:
            current_player_cards = taro_cards_sorted
        else:
            current_player_cards = hanako_cards_sorted

    remaining_hanako_cards = len(hanako_cards_sorted)
    remaining_taro_cards = len(taro_cards_sorted)

    return remaining_hanako_cards, remaining_taro_cards

def main(command_line_arguments):
    while True:
        total_cards_per_player = int(input())
        if total_cards_per_player == 0:
            break

        taro_cards_sorted = sorted([int(input()) for _ in range(total_cards_per_player)])
        all_possible_cards = set(range(1, 2 * total_cards_per_player + 1))
        hanako_cards_sorted = sorted(all_possible_cards - set(taro_cards_sorted))

        hanako_cards_left, taro_cards_left = play_card_game(taro_cards_sorted, hanako_cards_sorted)
        print(hanako_cards_left)
        print(taro_cards_left)

if __name__ == '__main__':
    main(sys.argv[1:])