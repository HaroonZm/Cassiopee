import sys

standard_input_readline = sys.stdin.readline
standard_output_write = sys.stdout.write

def is_winning_position(number_of_piles, lower_move_limit, upper_move_limit, pile_sizes_list):
    minimum_move_limit = min(lower_move_limit, upper_move_limit)
    nimber_xor = 0

    for current_pile_size in pile_sizes_list:
        nimber_xor ^= current_pile_size % (minimum_move_limit + 1)

    if lower_move_limit == upper_move_limit:
        return nimber_xor != 0

    if lower_move_limit > upper_move_limit:
        if nimber_xor != 0:
            return 1
        for current_pile_size in pile_sizes_list:
            if current_pile_size > upper_move_limit:
                return 1
        return 0

    pile_greater_than_lower_limit_count = 0
    last_large_pile_size = 1
    win_nimber_for_large_pile = 0

    for current_pile_size in pile_sizes_list:
        if current_pile_size > lower_move_limit:
            pile_greater_than_lower_limit_count += 1
            last_large_pile_size = current_pile_size
            win_nimber_for_large_pile = nimber_xor ^ (current_pile_size % (minimum_move_limit + 1))

    if pile_greater_than_lower_limit_count > 1:
        return 0

    if pile_greater_than_lower_limit_count == 0:
        return nimber_xor != 0

    return win_nimber_for_large_pile <= lower_move_limit and 1 <= last_large_pile_size - win_nimber_for_large_pile <= lower_move_limit

def main():
    number_of_piles, lower_move_limit, upper_move_limit = map(int, standard_input_readline().split())
    pile_sizes_list = [int(standard_input_readline()) for current_index in range(number_of_piles)]
    if is_winning_position(number_of_piles, lower_move_limit, upper_move_limit, pile_sizes_list):
        standard_output_write("Hanako\n")
    else:
        standard_output_write("Jiro\n")

main()