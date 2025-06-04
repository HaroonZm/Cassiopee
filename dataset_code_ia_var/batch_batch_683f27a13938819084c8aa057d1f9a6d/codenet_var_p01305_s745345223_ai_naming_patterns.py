import itertools

def process_test_cases():
    num_test_cases = int(input())
    permutation_count = 362880  # 9!
    for _ in range(num_test_cases):
        player_one_cards = list(map(int, input().split()))
        player_two_cards = list(map(int, input().split()))
        player_one_win_count = 0
        player_two_win_count = 0
        for player_two_hand in itertools.permutations(player_two_cards, 9):
            player_one_score = 0
            player_two_score = 0
            for card_one, card_two in zip(player_one_cards, player_two_hand):
                if card_one < card_two:
                    player_two_score += card_one + card_two
                else:
                    player_one_score += card_one + card_two
            if player_one_score > player_two_score:
                player_one_win_count += 1
            elif player_one_score < player_two_score:
                player_two_win_count += 1
        print(player_one_win_count / permutation_count, player_two_win_count / permutation_count)

process_test_cases()