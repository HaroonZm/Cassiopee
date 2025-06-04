import sys

def main():
    for input_line in get_input_lines():
        card_lis = parse_input_line(input_line)
        analyze_hand(card_lis)

def get_input_lines():
    return sys.stdin

def parse_input_line(input_line):
    return [int(char) for char in input_line.split(',')]

def analyze_hand(card_lis):
    result_dic = build_result_dic(card_lis)
    process_result(result_dic, card_lis)

def build_result_dic(card_lis):
    result_dic = {}
    check_num_lis = []
    working_lis = card_lis[:]
    for _ in range(5):
        check_num = get_first_elem(working_lis)
        if not is_in_list(check_num, check_num_lis):
            update_result_dic(result_dic, check_num, working_lis)
            append_to_list(check_num, check_num_lis)
        cycle_working_list(working_lis)
    return result_dic

def get_first_elem(lis):
    return lis[0]

def is_in_list(elem, lis):
    return elem in lis

def append_to_list(elem, lis):
    lis.append(elem)

def update_result_dic(result_dic, check_num, working_lis):
    for card in get_rest_of_list(working_lis):
        if card == check_num:
            if card in result_dic:
                result_dic[card] = increment_value(result_dic[card])
            else:
                result_dic[card] = 2

def get_rest_of_list(lis):
    return lis[1:]

def increment_value(value):
    return value + 1

def cycle_working_list(working_lis):
    elem = remove_first_elem(working_lis)
    working_lis.append(elem)

def remove_first_elem(lis):
    return lis.pop(0)

def process_result(result_dic, card_lis):
    result = get_result_values(result_dic)
    sort_list(result)
    if is_one_pair(result):
        print_result('one pair')
    elif is_two_pair(result):
        print_result('two pair')
    elif is_three_of_a_kind(result):
        print_result('three card')
    elif is_four_of_a_kind(result):
        print_result('four card')
    elif is_full_house(result):
        print_result('full house')
    elif is_result_empty(result):
        process_no_pair(card_lis)
    # else do nothing

def get_result_values(result_dic):
    return list(result_dic.values())

def sort_list(lis):
    lis.sort()

def is_one_pair(result):
    return result == [2]

def is_two_pair(result):
    return result == [2,2]

def is_three_of_a_kind(result):
    return result == [3]

def is_four_of_a_kind(result):
    return result == [4]

def is_full_house(result):
    return result == [2,3]

def is_result_empty(result):
    return not result

def process_no_pair(card_lis):
    copy_card_lis = card_lis[:]
    sort_list(copy_card_lis)
    if is_royal_straight(copy_card_lis):
        print_result('straight')
    elif is_straight(copy_card_lis):
        print_result('straight')
    else:
        print_result('null')

def is_royal_straight(card_lis):
    return card_lis == [1,10,11,12,13]

def is_straight(card_lis):
    check_num = card_lis[0]
    for card in card_lis:
        if card != check_num:
            return False
        check_num = card + 1
    return True

def print_result(message):
    print(message)

main()