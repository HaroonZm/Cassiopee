def get_input():
    return input()

def get_list_input():
    return input()

def split_string(s):
    return s.split()

def str_to_int_list(str_list):
    return [int(num) for num in str_list]

def initialize_score():
    return 0

def is_empty_list(lst):
    return len(lst) < 1

def find_max_in_list(lst):
    return max(lst)

def add_to_score(score, value):
    return score + value

def remove_from_list(lst, value):
    lst.remove(value)

def calculate_difference(score1, score2):
    return score1 - score2

def print_result(result):
    print(result)

def game_turn(a_list, score):
    next_num = find_max_in_list(a_list)
    score = add_to_score(score, next_num)
    remove_from_list(a_list, next_num)
    return score

def main_game():
    n = get_input()
    list_input_str = get_list_input()
    spl = split_string(list_input_str)
    a_list = str_to_int_list(spl)

    alice = initialize_score()
    bob = initialize_score()

    while True:
        if is_empty_list(a_list):
            break
        alice = game_turn(a_list, alice)
        if is_empty_list(a_list):
            break
        bob = game_turn(a_list, bob)

    result = calculate_difference(alice, bob)
    print_result(result)

main_game()